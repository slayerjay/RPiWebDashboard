import web 
import json 
import module_config

render = web.template.render('templates/', base='index')

class WebServer:
    def __init__(self):
        urls = ('/','root','/stats','Stats')
        self.app = web.application(urls,globals())
    
    def run(self):
        self.app.run()

class root:
    def GET(self):
        return render.index('')
 
class Stats:
    def GET(self):
        input = web.input(module="", params="")
        module = input.module
        params = input.params
        if module in module_config.modules:
            return json.dumps({module: module_config.modules[module].get(params)})
        return json.dumps(GeneralStats().get(params))
 
class GeneralStats:
    def get(self, params):
        result = {}
        for key in module_config.modules.keys():
            result[key.lower()] = module_config.modules[key].get(params)
        return result
