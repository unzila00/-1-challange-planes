#make a web app for a  war in which  user known  which planes are used to fight with enemy country 
## PAK AIR FORCE PLANES
class planes :
    def __init__(self):
        self.fighterJets = {
            "1" : "F-16 Fighting Falcon",
            "2" : "F-4 Phantom",
            "3" : "JF-17 Thunder"
            }
        self.bombers = {
    "1" : "B-2 Spirit",
    "2" : "B-52 Stratofortress" ,
    "B" : "B-1 Lancer"
}
        self. transportPlanes = {
            "1" :   "C-130  Hercules",
            "2" :   "VC-25A" ,
        
        }
        self.specializedPlanes = {
            "1" : "AC-130U" ,
            "2" : "A-10 Thunderbolt II" ,
            "3" : "U-2" ,
            "4" :   "YAL-1A",
            "5" : "F-117A Nightawk"
        }
        def  start(self):
            self.planes =  planes()
            self.planes.fighterJets =  planes.fighterJets
            self.planes.bombers  = planes.boombers
            self.planes.transportPlanes = planes.transportPlanes
            self.planes.specializedPlanes = planes.specializedPlanes
            self.planes.start()
            print("Welcome to the Pkaistan Air Force Plane Information System!")
            print("please select a category of planes to viewe")
            print("1.Fighter Jets")
            print("2.Bombers")
            print("3.Transport Planes")
            print("4.Specialized Planes")
            print("5.exit")
            while True:
                choice = input("Enter your choice (1-5):")
                if choice =="1":
                    self.viewFighterJets()
                elif choice =="2":
                    self.viewBombers()
                elif choice =="3":
                    self.viewTransportPlanes()
                elif choice =="4":
                    self.viewSpecializedPlanes()
                elif choice =="5":
                    print("Existing the system.")
                    break
                else:
                    print("Invalid choice. Please try again.")
                    def viewFighterJets(self):
                        print("Fighter Jets")
                        for key,value in self.fighterJets.items():
                            print(f"{key}.value")
                            def viewBombers(self):
                                print("Bombers")
                                for key,value in self.bombers.items():
                                    print(f"{key}.value")
                                    def viewTransportPlanes(self):
                                        print("Transport Planes")
                                        for key,value in self.transportPlanes.items():
                                            print(f"{key}.value")
                                            def viewSpecializedPlanes(self):
                                                print("Specialized Planes")
                                                for key,value in self.specializedPlanes.items():
                                                    print(f"{key}.value")
                                                    if __name__ == "__main__":
                                                        planes = planes()
                                                        planes.start()
                                                

                                    
                    


