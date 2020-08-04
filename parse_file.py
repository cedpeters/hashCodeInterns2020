class Endpoint:
	def __init__(self, id, datacenterLatency):
		self.id = id
		self.datacenterLatency = datacenterLatency
		self.links = []

	def set_videos(self, videos):
		self.videos = videos	

	def add_link(self, link):
		self.links.append(link)



class Link:
	def __init__(self, latency, cache, endpoint):
		self.latency = latency
		self.cache = cache
		self.endpoint = endpoint


class Cache:
	def __init__(self, sizeLimit, id):
		self.sizeLimit = sizeLimit
		self.id = id
		self.link = []

	def add_link(self, link):
		self.link.append(link)
	

def parse() -> dict:
    nVideos=0
    nEndpoints=0
    nRequests=0
    nCaches=0
    currentLine=0
    cacheSize=0
    videoSizes=0
    currentEndpoint = null
    nextEndpointId = 0
    endpoints = []
    caches: []
    latenciesLeft = 0
    with open(filename) as f:
        content = f.readlines()
        for line in content:
        	if(currentLine == 0):
        		values = line.split()
        		nVideos = int(values[0])
        		nEndpoints=int(values[1])
        		nRequests = int(values[2])
        		nCaches = int(values[3])
        		cacheSize=int(values[4])

        		for i in nCaches:
        			caches.append(Cache(cacheSize, i))

        	else if(currentLine == 1):
        		videoSizes = line.split()
        	
        	else if(!(endpoints.size == nEndpoints) || latenciesLeft != 0 ):
        		if(currentEndpoint == null):
        			endpointInfo = line.split()
        			currentEndpoint = Endpoint(nextEndpointId, int(endpointInfo[0]))
        			endpoints.append(currentEndpoint)
        			latenciesLeft = int(endpointInfo[1])

        		else:
        			if(latenciesLeft == 0)
        				currentEndpoint == null
        			latencyInfo = line.split()
        			newLink = Link(latencyInf0[1],caches[latencyInfo[0]], currentEndpoint)	
        			currentEndpoint.add_link(newLink)
        			caches[latencyInfo[0]].add_link(newLink)



        	else:
        			

        	currentLine++
        # TODO parse each line

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return data
