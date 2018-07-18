var app = angular.module('myApp', []);

app.run(function($rootScope, $http){
    $rootScope.processFormSubmit = function(){
        // var data =  {"timevalue": $rootScope.timevalue};
        // var url = "../cgi-bin/process-time.py";
        // $http.post(url, data).then(function(response){
            //     console.log(response.data);
            // });
            
        // var data = `timevalue=${$rootScope.timevalue}`;
        // var url = `../cgi-bin/process-time.py?${data}`;
        // $http.get(url).then(function(response){
            //     console.log(response.data);
            // });

        var data =  `timevalue=${$rootScope.timevalue}`;
        var url = "../cgi-bin/process-time.py";
        angular.element.post(url, data, function(response){
            response = JSON.parse(response);
            console.log(response);
        });
    };
});