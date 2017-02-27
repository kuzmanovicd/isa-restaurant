'use strict';

app.controller('RestaurantController', function ($scope, $location, $routeParams, RestaurantService) {
    
    RestaurantService.get($routeParams.id).success(function(data) {
        $scope.restaurant = data;
    });

    //dodavanje providera
    $scope.addProvider = function() {
        console.log('ceeeekksladkslkdlsad');
        $location.path('/provider/add');
    };

    //dodavanje randika
    $scope.addRadnik = function() {
        console.log('ceeeekksladkslkdlsad');
        $location.path('/employee/add');
    };

    $scope.getAll = function() {
        RestaurantService.getAll().success(function (data) {
            $scope.restaurants = data;
        });
    };


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
         ProviderService.create('provider', $scope.provider); 
    };
  
});





