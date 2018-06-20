import fpGrowth
simpDat = fpGrowth.loadSimpDat()
initSet = fpGrowth.createInitSet(simpDat)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
myFPtree.disp()