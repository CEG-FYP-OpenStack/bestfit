import sys

def bestfit(vm[], node[]):
	resultNode = None
	currentRatio = 1.0
	for n in node:
		diskRatio = (free_disk - vm['disk'])/totaldisk
		ramRatio = (free_ram - vm['ram'])/totalram
		vcpusRatio = (free_vcpus - vm['vcpus'])/totalvcpus
		if diskRatio > 0 and ramRatio > 0 and vcpusRatio > 0:
			totalRatio = w1*diskRatio + w2*ramRatio + w3*vcpusRatio
			if totalRatio < currentRatio :
				currentRatio = totalRatio
				resultNode = nodeName
	return resultNode

def bestfitwithmigration(vm[], node[]):
	detailedVM = []
	resultNode = None
	minMigrationList = []
	minNoOfMigration = sys.minint
	minMigrationData = sys.maxint
	resultNode = bestfit(vm,node)
	if resultNode == None :
		'''Feasible Node will get compute nodes with full capacity that can satify vm '''
		feasibleNode = node
		for n in feasibleNode:
			localMigrationList = []
			localNoOfMigration = 0
			localMigrationData = 0
			'''Get currently running VMs on this compute node sorted based on diskspace, RAM, vcpus '''
			vmList = detailedVM
			for v in vmList:
				destNode = bestfit(v, node - n)
				if destNode = 'None':
					continue
				else:
					localMigrationList.append([v,destNode])
					localNoOfMigration = localNoOfMigration + 1
					localMigrationData = localMigrationData + v['disk']
					'''Check with decreaded load wheter we can accomated the vm'''
					if True :
						flag = 1
						break
		if flag==1:
			if localNoOfMigration < minNoOfMigration:
				minNoOfMigration = localNoOfMigration
				minMigrationData = localMigrationData
				minMigrationList = localMigrationList
				resultNode = n.nodeName
			elif localNoOfMigration == minNoOfMigration:
				if localMigrationData < minMigrationData:
					minNoOfMigration = localNoOfMigration
					minMigrationData = localMigrationData
					minMigrationList = localMigrationList
					resultNode = n.nodeName
					