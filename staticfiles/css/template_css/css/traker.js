var settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total?country=India",
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "covid-19-coronavirus-statistics.p.rapidapi.com",
		"x-rapidapi-key": "5335f1a75cmsh5b8000e6ef0966bp1d9970jsnf5195f8554da"
	}
}

$.ajax(settings).done(function (response) {

    document.querySelector("#app1").innerHTML= response.data.confirmed
    document.querySelector("#app2").innerHTML= response.data.recovered
    document.querySelector("#app3").innerHTML= response.data.deaths
});



