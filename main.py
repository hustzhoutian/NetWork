#-*- coding: UTF-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import random

n = 100   #n个节点
p = 0.2   #概率0.2生成ER图
index = 0
p1 = 0.1  #点攻击规模10%
addnodeaccout = int(n*0.1)

def addnode(n1,n2,G):
    for i in range(n1,n1+n2):
        G.add_node(i)

def getaddcodelist(n1,n2,list):
    for i in  range(n1,n1+n2):
        list.append(i)

def addedgeforlist(list1,list2,G):
    for i in list1:
        for j in list2:
            if(random.random()<0.5):
                G.add_edge(i,j)

def DegreeTopN(G1,G2,n):
    list1 = sorted(nx.degree_centrality(G1).items(), key=lambda d:d[1],reverse=True)
    list2 = sorted(nx.degree_centrality(G2).items(), key=lambda d:d[1],reverse=True)
    toplist1 = []
    toplist2 = []
    index1 = 0
    index2 = 0
    for i in list1:
        toplist1.append(i[0])
        index1 += 1
        if(index1==n):
            break
    for j in list2:
        toplist2.append(j[0])
        index2 += 1
        if(index2==n):
            break
    return len(set(toplist1).intersection(set(toplist2)))/(1.0*n)

def BetweennessTopN(G1,G2,n):
    list1 = sorted(nx.betweenness_centrality(G1).items(), key=lambda d:d[1],reverse=True)
    list2 = sorted(nx.betweenness_centrality(G2).items(), key=lambda d:d[1],reverse=True)
    #print list1
    #print list2
    toplist1 = []
    toplist2 = []
    index1 = 0
    index2 = 0
    for i in list1:
        toplist1.append(i[0])
        index1 += 1
        if(index1==n):
            break
    for j in list2:
        toplist2.append(j[0])
        index2 += 1
        if(index2==n):
            break
    return len(set(toplist1).intersection(set(toplist2)))/(1.0*n)

def ClosenessTopN(G1,G2,n):
    list1 = sorted(nx.closeness_centrality(G1).items(), key=lambda d:d[1],reverse=True)
    list2 = sorted(nx.closeness_centrality(G2).items(), key=lambda d:d[1],reverse=True)
    toplist1 = []
    toplist2 = []
    index1 = 0
    index2 = 0
    for i in list1:
        toplist1.append(i[0])
        index1 += 1
        if(index1==n):
            break
    for j in list2:
        toplist2.append(j[0])
        index2 += 1
        if(index2==n):
            break
    return len(set(toplist1).intersection(set(toplist2)))/(1.0*n)

def EigenvectorTopN(G1,G2,n):
    list1 = sorted(nx.eigenvector_centrality(G1).items(), key=lambda d:d[1],reverse=True)
    list2 = sorted(nx.eigenvector_centrality(G2).items(), key=lambda d:d[1],reverse=True)
    toplist1 = []
    toplist2 = []
    index1 = 0
    index2 = 0
    for i in list1:
        toplist1.append(i[0])
        index1 += 1
        if(index1==n):
            break
    for j in list2:
        toplist2.append(j[0])
        index2 += 1
        if(index2==n):
            break
    return len(set(toplist1).intersection(set(toplist2)))/(1.0*n)

ER = nx.random_graphs.erdos_renyi_graph(n,p) #生成包含50个节点、以概率0.2连接的随机图
ER1 = ER.copy()
list1 = sorted(nx.degree_centrality(ER).items(), key=lambda d:d[1],reverse=False)
list2 = []
list3 = []
for each in list1:
    list2.append(each[0])
    index += 1
    if (index == int(n * 0.1)):
        break
addnode(n,addnodeaccout,ER1)
getaddcodelist(n,addnodeaccout,list3)
addedgeforlist(list2,list3,ER1)
print DegreeTopN(ER,ER1,1),DegreeTopN(ER,ER1,3),DegreeTopN(ER,ER1,int(n*0.1))
print BetweennessTopN(ER,ER1,1),BetweennessTopN(ER,ER1,3),BetweennessTopN(ER,ER1,int(n*0.1))
print ClosenessTopN(ER,ER1,1),ClosenessTopN(ER,ER1,3),ClosenessTopN(ER,ER1,int(n*0.1))
print EigenvectorTopN(ER,ER1,1),EigenvectorTopN(ER,ER1,3),EigenvectorTopN(ER,ER1,int(n*0.1))
#pos = nx.shell_layout(ER1)
#nx.draw(ER1,pos,with_labels=False,node_size = 30)
#plt.show()






#print nx.degree_centrality(ER)
#pos = nx.shell_layout(ER)          #定义一个布局，此处采用了shell布局方式
#nx.draw(ER,pos,with_labels=False,node_size = 30)
#plt.show()