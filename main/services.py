from django.shortcuts import render

#METHOD TO RENDER PAGES WITH ANY CONTEXT
#ASSUMES THAT PATH HAS BEEN SET PROPERLY
#ASSUMES THAT RENDERDATA OBJECT CONTAINS REQUEST, PATH, AND CONTEXT OBJECT 
def renderPage(renderData): 
    if not renderData['request']: 
        return 'No request provided'
    if not renderData['path']:
        return 'No template path provided'
    if not renderData['context']: 
        return render(renderData['request'], renderData['path'])
    return render(renderData['request'], renderData['path'], renderData['context'])


#METHOD CONVERTS GIVEN REQUEST PATH TO HTML
def convertPathToHtml(path): 
    return path[1:] + '.html'