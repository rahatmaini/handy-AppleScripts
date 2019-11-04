import subprocess
import os

baseSavedSearchPath = "/Users/rahat/Library/Saved Searches/"

output = subprocess.check_output(['ls',baseSavedSearchPath])
savedSearches = str(output).replace("b'",'').replace("'","").strip("\\n").split("\\n")


namesAndQueries={}


for i in savedSearches: #in each saved search

    rawQuery=str(subprocess.check_output(['cat',baseSavedSearchPath+i])).replace("\\n","").replace("\\t","").replace("&amp;","&")
    rawQuery=rawQuery[rawQuery.find("<key>RawQuery</key><string>")+27:rawQuery.find("</str")]
    
    tagName=i[:i.find(".")]

    namesAndQueries[tagName]=rawQuery


for tag in namesAndQueries: #iterate through dictionary of savedSearch:searchQuery
    
    rawResults=str(subprocess.check_output(['mdfind',namesAndQueries[tag]])).replace("b'",'').replace("'","").strip("\\n").split("\\n")
    
    for item in rawResults:
        testString="tag --add "+"'"+tag+"' '"+item+"'"
        #print (testString)
        os.system(testString)



