'use strict';

app.controller('RestaurantController', function ($scope, $rootScope, $location, $routeParams, RestaurantService, BasicUserService) {
    
    RestaurantService.get($routeParams.id).success(function(data) {
        $scope.restaurant = data;
    });

    //dodavanje providera
    $scope.addProvider = function() {
        console.log('addProvider');
        $location.path('/provider/add');
    };

    //dodavanje randika
    $scope.addRadnik = function() {
        console.log('addRadnik');
        $location.path('/employee/add');
    };

    //dodavanje regiona
     $scope.addRegion = function() {
        console.log('addRegion');
        $location.path('/region/add');
    };

    $scope.getAll = function() {
        RestaurantService.getAll().success(function (data) {
            $scope.restaurants = data;
        });
    };

    if($rootScope.currentUser.user_type == 'RM') {
        BasicUserService.getRestaurantManager($rootScope.currentUser.id).success(function (data) {
            RestaurantService.get(data.working_in).success(function(data) {
                $scope.restaurant = data;
            });
        });
    }


});


//kontroler za radnika
app.controller('RadnikController', function ($scope, RadnikService) {
    //WA - Waiter
    //BA - Bartender
    //C0 - Cook
    $scope.employee_types = ['WA', 'BA', 'CO'];

    $scope.create = function() {
        if($scope.employee.type == 'WA') {
            RadnikService.create('waiter', $scope.employee);
        }

        if($scope.employee.type == 'BA') {
            RadnikService.create('bartender', $scope.employee);
        }

        if($scope.employee.type == 'CO') {
            RadnikService.create('cook', $scope.employee);
        }
        
    };
  
});

//kontroler za Providera
app.controller('ProviderController', function ($scope, $location, ProviderService) {

    $scope.create = function() {
         ProviderService.create($scope.provider).success(function(data) {
             $location.path('/');
         }); 
    };
  
});


//kontroler za stolove
app.controller('TableController', function($scope, TableService){
    $scope.getRegions = function() {
        TableService.getRegions().success(function(data) {
           $scope.regions = data;
        });
    }

    $scope.reserve = function (id) {
        console.log(id);
    };

})



//kontroler za Region
app.controller('RegionController', function ($scope, $location, RegionService) {

    $scope.region = {};
    $scope.region.is_open = false;
    $scope.region.is_forSmoke = false;

    $scope.create = function() {
        $scope.region.is_frontSide = true;
        console.log($scope.region);
        RegionService.create($scope.region).success(function(data) {
            $location.path('/');
        }); 
    };

    //console.log(angular.toJson(region));
  
});



