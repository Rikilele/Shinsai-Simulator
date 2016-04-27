# scene == the app's main window (self)
# importing panda3d modules and classes
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import *
from pandac.PandaModules import WindowProperties

class Building(ShowBase):
    def __init__(self, scene, name, posX, posY, posZ):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        if name == "concrete": self.buildConcrete(scene)
        elif name == "R": self.buildRBuilding(scene)
        elif name == "house1": self.buildHouse1(scene)
        elif name == "house2": self.buildHouse2(scene)
        elif name == "house3": self.buildHouse3(scene)
        elif name == "tower": self.buildTower(scene)
        elif name == "build": self.buildBuild(scene)
        elif name == "cafe": self.buildCafe(scene)
        elif name == "old": self.buildOld(scene)

    def buildHouse1(self, scene):
        self.building = scene.loader.loadModel("models/house/house1/house1.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(130)
        self.building.setHpr(90,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildHouse2(self, scene):
        self.building = scene.loader.loadModel("models/house/house2/house2.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(130)
        self.building.setHpr(90,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildHouse3(self, scene):
        self.building = scene.loader.loadModel("models/house/house3/house3.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(130)
        self.building.setHpr(90,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)
    
    def buildTower(self, scene):
        self.building = scene.loader.loadModel("models/tower/tower.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(100)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildConcrete(self, scene):
        self.building = scene.loader.loadModel("models/concrete/concrete.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(850)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildRBuilding(self, scene):
        self.building = scene.loader.loadModel("models/r/r-building.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(850)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildBuild(self, scene):
        self.building = scene.loader.loadModel("models/build/build.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(80)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildCafe(self, scene):
        self.building = scene.loader.loadModel("models/cafe/cafe.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(40)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)

    def buildOld(self, scene):
        self.building = scene.loader.loadModel("models/oldbuild/oldbuild.egg")
        self.building.reparentTo(scene.render)
        self.building.setScale(30)
        self.building.setHpr(0,0,0)
        self.building.setPos(self.posX, self.posY, self.posZ)
        self.building.setTwoSided(True)
