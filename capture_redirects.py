from selenium import webdriver
from browsermobproxy import Server

server = Server(environment.b_mob_proxy_path)
server.start()
proxy = server.create_proxy()
service_args = ["--proxy-server=%s" % proxy.proxy]
driver = webdriver.PhantomJS(service_args=service_args)

proxy.new_har()
driver.get('url_to_open')
print proxy.har  # this is the archive
# for example:
all_requests = [entry['request']['url'] for entry in proxy.har['log']['entries']]