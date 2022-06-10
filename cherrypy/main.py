import cherrypy


class Application(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"Hello": "World"}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def users(self):
        new_user = cherrypy.request.json
        return_value = f'{new_user["name"]},{new_user["age"]},{new_user["location"]},'
        return {"data": "".join([return_value for _ in range(0, 1024)])}


app = cherrypy.Application(Application(), "/")

if __name__ == "__main__":
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.quickstart(Application())
