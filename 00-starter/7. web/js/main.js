var app = angular.module('myApp', []);

app.run(function($rootScope, $http){
    angular.element("#show_athlete").hide();
    angular.element("#click_show_athlete").on('click', function(){
        angular.element("#view_athlete").hide();
        angular.element("#show_athlete").toggle();
    });
    
    angular.element("#view_athlete").hide();

    var url = "../cgi-bin/generate_list.py";
    $http.get(url).then(function(response){
        $rootScope.athletes = response.data;
    });
    
    $rootScope.athleteSubmit = function(){
        data = angular.element("[name='athlete']:checked").val();
        if(data.length != 0){
            data = "dob=" + data;
            url = "../cgi-bin/generate_timing_data.py?" + data;
            $http.get(url).then(function(response){
                $rootScope.records = response.data[0];
                console.log($rootScope.records);
                angular.element("#show_athlete").hide();
                angular.element("#view_athlete").show();
            });
        }
    };
});

app.directive("showAthlete", function(){
    return {
        restrict: 'AEC',
        templateUrl: "../template/show_athlete.html"
    }   
});

app.directive("viewAthlete", function(){
    return{
        restrict: 'AEC',
        templateUrl: "../template/view_athlete.html"
    }
})