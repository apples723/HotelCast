# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
#django imports 
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.http import HttpResponse
import os
#guidebox library
import guidebox
#setup guidebox
#So my api key is not on github...
if os.name == "nt":
	KeyDoc = open("../../guidebox_api_key.txt", 'r')
else:
	KeyDoc = open("/home/guidebox_api_key.txt", 'r') 
api_key = KeyDoc.read()
api_key = api_key.strip('\n')
guidebox.api_key = api_key

#render index
def index(request):
	return render(request, 'index.html')

#Guidebox Stuff

#results class
class SearchResults:
	def __init__(self,id):
		self.id = id
		self.title = None
		self.img = None
	def add_data(self,id,title,img,bio):
		self.id = id
		self.title = title
		self.img = img 
		self.bio = bio
class ShowObject:
	def __init__(self,id):
		self.id = id
		self.title = None
		self.img = None
	def add_data(self,id,title,img_lg,bio):
		self.id = id
		self.title = title
		self.img_lrg = img_lg
		self.bio = bio
class MovieObject:
	def __init__(self,id):
		self.id = id
		self.title = None
		self.img = None
	def add_data(self,id,title,img_lg,bio,netflix,hulu,amazon):
		self.id = id
		self.title = title
		self.img_lrg = img_lg
		self.bio = bio
		self.netflix = netflix
		self.hulu = hulu
		self.amazon = amazon
class SeasonObject:
	def __init__(self,id):
		self.id = id
		self.title = None
		self.img = None
	def add_data(self,id,ses_num,title,img,bio,url):
		self.id = id
		self.title = title
		self.img = img
		self.bio = bio		
		self.url = url
		self.season_number = ses_num
		
		
def search_show(request):
	query =  request.GET.get('query')
	results = guidebox.Search.shows(feild='title',query=query)
	results = results.results
	result_dict = dict()
	for result in results:
		id = result.id
		title = result.title 
		img = result.artwork_208x117
		show_bio = guidebox.Show.retrieve(id=id)
		bio = show_bio.overview
		result_dict[id] = SearchResults(id)
		result_dict[id].add_data(id,title,img,bio)
	search_type = "show"
	return render(request, 'search.html', {'search_type':search_type, 'results':result_dict}) 

def search_movie(request):
	query =  request.GET.get('query')
	results = guidebox.Search.movies(feild='title',query=query)
	results = results.results
	result_dict = dict()
	for result in results:
		id = result.id
		title = result.title 
		img = result.poster_240x342
		show_bio = guidebox.Movie.retrieve(id=id)
		bio = show_bio.overview
		result_dict[id] = SearchResults(id)
		result_dict[id].add_data(id,title,img,bio)
	search_type = "movie"
	return render(request, 'search.html', {'search_type':search_type, 'results':result_dict}) 	
def movie_info(request):
	movie_id = request.GET.get('id')
	movie_info = guidebox.Movie.retrieve(id=movie_id,include_links=True)
	movie_dict = dict()
	img_lrg = movie_info.poster_400x570
	movie_title = movie_info.title
	movie_bio = movie_info.overview
	#prefill links to none
	netflix = None
	amazon = None
	hulu = None
	for obj in movie_info.subscription_web_sources:
		if(obj.source == "netflix"):
			url = obj.link
			url = url.replace('Movie','watch')
			url = url.replace('movies.','')
			netflix = url
		if(obj.source == "amazon_prime"):
			amazon = obj.link
		if(obj.source == "hulu_plus"):
			hulu = obj.link
	movie_dict[movie_id] = MovieObject(movie_id)
	movie_dict[movie_id].add_data(movie_id,movie_title,img_lrg,movie_bio,netflix,hulu,amazon)
	return render(request,'movie.html', {'title': movie_title, 'movie_info':movie_dict})	
	
	

def show_info(request):
	show_id = request.GET.get('id')
	show_info = guidebox.Show.retrieve(id=show_id)
	show_dict = dict()
	img_lrg = show_info.artwork_608x342
	show_title = show_info.title
	bio = show_info.overview
	show_dict[show_id] = ShowObject(show_id)
	show_dict[show_id].add_data(show_id,show_title,img_lrg,bio)
	#episode info
	episodes = guidebox.Show.episodes(id=show_id,season=1,reverse_ordering=True,include_links=True)
	results = episodes.results
	result_dict = OrderedDict()
	for result in results:
		id = result.id
		title = result.original_title
		img = result.thumbnail_400x225
		bio = bio
		ses_num = result['season_number']
		url = result['subscription_web_sources']
		netflix_status = "no"
		for obj in url:
			if obj['source'] == "netflix":
				netflix_status = "yes"
				url = obj['link']
				url = url.replace('Movie','watch')
				url = url.replace('movies.','')
			if obj['source'] == "hulu_plus":
				url = obj['link']
		result_dict[id] = SeasonObject(id)
		result_dict[id].add_data(id,ses_num,title,img,bio,url)
	return render(request,'show.html', {'title': show_title, 'show_info':show_dict, 'episodes': result_dict, 'netflix_status': netflix_status})
def write_command(request):
	command = request.GET.get('command');
	import os
	command_file = open(os.path.join(os.path.dirname(__file__), 'command.txt'), 'w')
	command_file.write(command)
	command_file.close()
	data = {
        'success_message': "true"
	}
	return JsonResponse(data)
def get_command(request):
	content = open(os.path.join(os.path.dirname(__file__), 'command.txt'), 'r')
	content = content.read()
	return HttpResponse(content, content_type='text/plain')
def remote(request):
	return render(request, 'remote.html')
	
#error views
def not_found(request):
    return render(request, 'errors/error_404.html')
def server_error(request):
    return render(request, 'errors/error_500.html')
 
def permission_denied(request):
    return render(request, 'errors/error_403.html')
 
def bad_request(request):
    return render(request, 'errors/error_400.html')
