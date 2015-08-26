import sys
from fileutil import *
from kazoo.client import KazooClient
import json
from wabbit_wappa import *
from subprocess import call

'''
get below from zookeeper

rules:
namespace feature type

namespace : default or name
feature : name of feature
transform : 
   split
   idx_val

{"rules":{"f1":"|split","f2":"ns1|"}}

otherwise will treat as string or float as given
   
'''
class JsonToVW:

    def transform(self,json,rules):
        for k in json:
            print k,json[k]

class VWSeldon:

    def __init__(self, conf):
        self.client = conf['client']
        self.awsKey = conf.get('awsKey',None)
        self.awsSecret = conf.get('awsSecret',None)
        self.zk_hosts = conf.get('zkHosts',None)
        if self.zk_hosts:
            print "connecting to zookeeper at ",self.zk_hosts
            self.zk_client = KazooClient(hosts=self.zk_hosts)
            self.zk_client.start()
        else:
            self.zk_client = None
        print "command line conf ",conf
        self.conf = self.__merge_conf(self.client,conf)
        print "conf after zookeeper merge ",conf
        self.create_vw(self.conf)
        self.features = self.conf.get('features',{})
        self.fns = self.conf.get('namespaces',{})
        self.include = self.conf.get('include',[])
        if 'target' in conf:
            self.features[self.conf['target']] = "label"
            self.target= self.conf['target']
        self.exclude = self.conf.get('exclude',None)
        self.weights = self.conf.get('weights',None)
        self.target_readable = self.conf.get('target_readable',None)



    def activateModel(self,client,folder):
        node = "/all_clients/"+client+"/vw"
        print "Activating model in zookeper at node ",node," with data ",folder
        if self.zk_client.exists(node):
            self.zk_client.set(node,folder)
        else:
            self.zk_client.create(node,folder,makepath=True)


    def __merge_conf(self,client,conf):
        thePath = "/all_clients/"+client+"/offline/vw"
        if self.zk_client and self.zk_client.exists(thePath):
            print "merging conf from zookeeper"
            data, stat = self.zk_client.get(thePath)
            zk_conf = json.loads(data.decode('utf-8'))
            zk_conf.update(conf)
            return zk_conf
        else:
            return conf


    def convertJsonFeature(self,conversion,ns,name,val):
        if conversion == "split":
            f = val.split()
            ns = ns + f
        elif isinstance(val, basestring):
            ns.append(val)
        else:
            ns.append((name,float(val)))

    def jsonToVw(self,j,tag=None):
        ns = {}
        for k in set(self.fns.values()):
            if not k == "label":
                ns[k] = []
        ns['def'] = []
        label = None
        importance = 1.0
        for k in j:
            if self.exclude and k in self.exclude:
                continue
            if self.include and not k in self.include and not k in self.features:
                continue
            if not k in self.fns:
                self.fns[k] = 'def'
            ns_f = ns[self.fns[k]]
            if k in self.features:
                conversion = self.features[k] 
                if conversion == "split":
                    self.convertJsonFeature(conversion,ns_f,k,j[k])                    
                elif conversion == "label":
                    label = int(j[k])
                    if self.weights and j[k] in self.weights:
                        importance = self.weights[j[k]]
            else:
                if isinstance(j[k], list):
                    for v in j[k]:
                        if isinstance(v,basestring):
                            self.convertJsonFeature(None,ns_f,k,v)
                        else:
                            self.convertJsonFeature(None,ns_f,k,k+str(v))
                elif isinstance(j[k], dict):
                    for k2 in j[k]:
                        self.convertJsonFeature(None,ns_f,k2,j[k][k2])
                else:
                    self.convertJsonFeature(None,ns_f,k,j[k])
        namespaces = []
        for k in ns:
            if not k == 'def':
                namespaces.append(Namespace(name=k,features=ns[k]))
        if len(ns['def']) == 0 and len(ns) == 1:
            return None
        if len(ns['def']) == 0:
            ns['def'] = None
        if self.weights:
            return self.vw2.make_line(response=label,importance=importance,tag=tag,features=ns['def'],namespaces=namespaces)
        else:
            return self.vw2.make_line(response=label,tag=tag,features=ns['def'],namespaces=namespaces)
        
    def create_vw(self,conf):
        vwArgs = conf.get('vwArgs',"")
        command = "vw --save_resume --predictions /dev/stdout --quiet "+vwArgs + " --readable_model ./model.readable"
        print command
        self.vw2 =  VW(command=command)
        print self.vw2.command

    def process(self,line):
        j = json.loads(line)
        vwLine = self.jsonToVw(j)
        self.numLinesProcessed += 1
        if vwLine:
            if self.target_readable:
                self.target_map[j[self.target]] = j[self.target_readable]
            if self.train_file:
                self.train_file.write(vwLine+"\n")
            else:
                self.vw2.send_line(vwLine)
        
    def save_target_map(self):
        v = json.dumps(self.target_map,sort_keys=True)
        f = open('./target_map.json',"w")
        f.write(v)
        f.close()


    def train(self,train_filename=None,vw_command=None):
        self.numLinesProcessed = 0
        self.target_map = {}
        if train_filename:
            self.train_file = open(train_filename,"w")
        else:
            self.train_file = None
        #stream data into vw
        inputPath = self.conf["inputPath"] + "/" + self.client + "/features/" + str(self.conf['day']) + "/"
        print "inputPath->",inputPath
        fileUtil = FileUtil(key=self.awsKey,secret=self.awsSecret)
        fileUtil.stream(inputPath,self.process)

        # save vw model
        if train_filename:
            self.vw2.close()
            self.train_file.close()
            r = call(["vw","--data",train_filename,"-f","model","--cache_file","./cache_file","--readable_model","./model.readable"]+self.conf['vwArgs'].split())
            print "called and got ",r
        else:
            self.vw2.save_model("./model")
            self.vw2.close()
            print "lines processed ",self.numLinesProcessed

        self.save_target_map()
        # copy models to final location
        outputPath = self.conf["outputPath"] + "/" + self.client + "/vw/" + str(self.conf["day"])
        print "outputPath->",outputPath
        fileUtil.copy("./model",outputPath+"/model")
        fileUtil.copy("./model.readable",outputPath+"/model.readable")
        fileUtil.copy("./target_map.json",outputPath+"/target_map.json")

        #activate model in zookeeper
        if "activate" in self.conf and self.conf["activate"]:
            self.activateModel(self.client,str(outputPath))