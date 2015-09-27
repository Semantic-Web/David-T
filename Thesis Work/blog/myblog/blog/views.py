# Create your views here.
import matplotlib.pyplot as plt
from pandas import *

import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader

def graph (request):
    x=[1,2,3,4,5,6]
    y=[5,2,6,8,3,4]
    plt.plot(x,y, linewidth=2)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('sample graph')
    plt.grid(True)
    #plt.show()
    
    plt.buffer = StringIO.StringIO()
    plt.canvas = plt.get_current_fig_manager().canvas
    plt.canvas.draw()
    plt.graphIMG = PIL.Image.fromstring("RGB", plt.canvas.get_width_height(), plt.canvas.tostring_rgb())
    plt.graphIMG.save(plt.buffer,"PNG")
    plt.close()
    return HttpResponse(plt.buffer.getvalue(), content_type= "image/png")
	
	