#!/usr/bin/env python
import web 
import json 
from server import WebServer

if __name__ == "__main__":
    webServer = WebServer()    
    webServer.run()
