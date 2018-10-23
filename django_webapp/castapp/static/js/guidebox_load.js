
function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}


$(function(){
	var show_id = getUrlVars()["id"];
	var api_key = "b8164d1dad070aa1840c4670c661ed63c0ee0bc1"	
	$.getJSON("https://api-public.guidebox.com/v2/shows/" + show_id + "/episodes?api_key=" + api_key, function(json1){
			num_season = json1.results[0].season_number;
			for (i = 2; i <= num_season; i = i + 1) {
				s_num = i;
				$("#season_dropdown").append('<option value="' + i + '">Season' + i + '</option>');
		};
	});
	
	$("#season_dropdown").change(function(){
			var season = this.value;
			$("#season_row").empty()
			$.getJSON("https://api-public.guidebox.com/v2/shows/" + show_id + "/episodes?api_key=" + api_key + "&include_links=true&season=" + season , function(json){
					$.each(json.results, function(d, item){
						title = item.original_title;
						img = item.thumbnail_400x225;
						urls = item.subscription_web_sources;
						netflix_status = $("#netflix_status").attr("data");
						if(netflix_status == "true"){
							$.each(urls, function(i, item){
								source = item.source;
								var netflix = "netflix";
								if(source == netflix){
									url = item.link;
									url = url.replace("movies.", "");
									url = url.replace("Movie","watch");
									$("#season_row").append('<div class="col-md-3 col-sm-6 mb-4"><span id="actionLink" data="' + url + '"><img class="img-fluid" src="' + img +'" alt=""></span><p>' + title + '</p></div>');
								}
							});
					  }
					  else{
						$.each(urls, function(i, item){
							source = item.source;
							console.log(source);
							var hulu_plus = "hulu_plus";
							if(source == hulu_plus){
								url = item.link;
								$("#season_row").append('<div class="col-md-3 col-sm-6 mb-4"><span id="actionLink" data="' + url + '"><img class="img-fluid" src="' + img +'" alt=""><p>' + title + '</p></div>');
							}
						});
					  }
						
			
					});
				
			});
	});
	
});