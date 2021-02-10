"""
    Name:        Inspector.py
    Author:      Aud#9488
    Description: This file just tracks the logs coming in from the workshop
"""

import os       #For file management
import pathlib  #For file stats
import datetime #For time thingies
import time     #For doin the sleepies
import math     #For calculations of some kind
import re       #reeeeeeeeeeeee


#Setup the workshop path based off of the user's windows name
WorkshopPath = os.path.join(os.path.expandvars("%userprofile%"),"Documents\\Overwatch\\Workshop")


def LogChanges(ListOfChanges, ServerLoad, LoadList, TotalEntries):
    #Check changes
    if len(ListOfChanges) == 0:
        return

    #Log 
    os.system("cls")
    print("[Server Load]:       {}".format(ServerLoad))
    print("[Total Log Entries]: {}\n\n".format(TotalEntries))


    #Find longest change
    Longest = 0
    for Changes in ListOfChanges:
        if len(Changes) > Longest: 
            Longest = len(Changes)

    #Don't let longest be over 80
    if Longest > 80:
        Longest = 80 + 4


    #Create top and bottom border
    Border = "+"

    for x in range(0, Longest + 1):
        Border += "-"

    Border += "+"

    #Go through changes
    print("[Last Logs]")

    print(Border)

    for Changes in ListOfChanges:
        LineToPrint = "| {}".format(Changes[0:80])

        #Calc the distance to border
        if len(Changes) < 80:
            for x in range(len(Changes), Longest):
                LineToPrint += " "

            LineToPrint += "|"

        else:
            LineToPrint += "... |"


        #print
        print(LineToPrint)


    #print border again
    print(Border)

    #Track rate of change of load
    print("\n\n")
   
    Height         = 10                #The height of the graph
    MaxLoad        = 300               #Max value a graph can have 
    HeightInterval = MaxLoad / Height  #The value interval for each Y entry 
    LayerHeight = 0

    Data = []

    #Create Data layers
    while(LayerHeight < MaxLoad):
        Row = []

        #Populate row 
        for x in range(0, 80):
            Row.append(" ")

        Data.append(Row)

        LayerHeight += HeightInterval


    #Add real data to it
    for EntryInt in range(0, len(LoadList)):
        Load = int(LoadList[EntryInt])

        #If it's over 300 it belong on the max row
        if Load > 300:
            Data[len(Data) - 1][EntryInt] = "+"

        #Else find the row it belongs on 
        else:
            Level = Height - math.floor(Load / HeightInterval)

            #If this is the last item
            if EntryInt == len(LoadList) - 1:
                Data[Level][EntryInt] = "."

            #If this isn't the last item figured out if we went up next
            else:
                NextLoad = int(LoadList[EntryInt + 1])
                NextLevel = Height - math.floor(NextLoad / HeightInterval)

                #If no change in level
                if NextLevel == Level:
                    Data[Level][EntryInt] = "_"

                #If it went down
                if NextLevel > Level:
                    Data[Level + 1][EntryInt] = "\\"

                #If it went up 
                if NextLevel < Level:
                    Data[Level][EntryInt] = '/'
                    

        

    #Now show :D 
    print("[Server load!!]")
    print(Border)

    RowDescriptor = MaxLoad
    for Rows in Data:
        Row = "".join(Rows)

        print("| {}    | - {}".format(Row, RowDescriptor))

        RowDescriptor -= HeightInterval



    print(Border)



    #Done



def TrackChanges(Filename):
    #Open the file 
    LastLength   = 0
    LastLoad     = 0
    TotalEntries = 0

    ListOfLoads = []
    ToBePrinted = []

    while(True):
        File = open(Filename, "r")

        #Read the lines 
        Lines = File.readlines()

        #Check the length of lines
        if(len(Lines) != LastLength):
            #Log the difference
            for LineInt in range(LastLength, len(Lines)):
                #Remove past 
                if len(ToBePrinted) > 20:
                    ToBePrinted.pop(0)

                #Add
                ToBePrinted.append(Lines[LineInt].strip('\n'))
                TotalEntries += 1

            #Save teh difference
            LastLength = len(Lines)

        #If they were the same just wait 
        else:
            time.sleep(1)

        #Check to be printed for server load
        for Lines in ToBePrinted:
            BreakDown = re.findall('\[[^\]]*\]', Lines)
            if len(BreakDown) > 2 and BreakDown[1] == "[SERVER_LOAD]":
                LastLoad = re.findall('\[[^\]]*\]', Lines)[2].strip("[").strip("]")
                ListOfLoads.append(LastLoad)

                #IF list too large, cut it 
                if len(ListOfLoads) > 80:
                    ListOfLoads.pop(0)


        #Log changes
        LogChanges(ToBePrinted, LastLoad, ListOfLoads, TotalEntries)

        #Close the file 
        File.close()








def Main():
    #Clear
    os.system("cls")

    #Initial pass through, check workshop existence
    if(os.path.exists(WorkshopPath) != True):
        print("[Error]: Workshop path {} doesn't exist on disk, is the log to file feature turned on in OW || Is your OW install modified?")


    #Now tha we know the file exist, find the most up to date files within the hour
    #And wait until one of these files change
    File       = None
    FilesFound = []

    print("[Welcome to the OWF Debugging tool... Basically just lets us see the incoming lines and server load]")
    print("[NOTE] The program will only start once a line has been written to a workshop log\n\n")
    print("[Searching for file] Looking for changes in files located in {}".format(WorkshopPath))

    while(File == None):
        #Search through files for new files
        for Files in os.listdir(WorkshopPath):
            Filename = os.path.join(WorkshopPath, Files)

            if(os.path.isfile(Filename)):
                #Check to see if the files found
                Found = False
                for CurrentFiles in FilesFound:
                    if CurrentFiles["Name"] == Filename:
                        Found = True


                #If not found, append it 
                if Found == False:
                    FilePathState = pathlib.Path(Filename)

                    FilesFound.append(
                        {
                            "Name" : Filename,
                            "LastEdited" : datetime.datetime.fromtimestamp(FilePathState.stat().st_mtime)
                        }
                    )


        #Search through found files and compare their old edits to now 
        for Files in FilesFound:
            #Setup Filestate
            FileState    = pathlib.Path(Files["Name"])
            NewTimestamp = datetime.datetime.fromtimestamp(FileState.stat().st_mtime)

            #Compare
            if(Files["LastEdited"] != NewTimestamp):
                #This is the file we'll be running with
                File = Files
                break

        #Sleep
        time.sleep(1)

    #We found the file lets go 
    print("[File Found] {} \n\t Assuming this is our target, begining loop on it".format(File["Name"]))

    TrackChanges(File["Name"])
    



#Start
Main()