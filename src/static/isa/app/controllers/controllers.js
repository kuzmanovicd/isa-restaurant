'use strict';

app.controller('RestaurantController', function ($scope, $location, RestaurantService) {
    
    RestaurantService.get(1).success(function(data) {
        //console.log(data);
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

});


//kontroler za radnika
app.controller('RadnikController', function ($scope, RadnikService) {
    //WA - Waiter
    //BA - Bartender
    //C0 - Cook
    $scope.employee_types = ['WA', 'BA', 'CO'];

    $scope.create = function() {
        if($scope.employee.type == 'WA') {
            RadnikService.create('provider', $scope.employee);
        }

        if($scope.employee.type == 'BA') {
            RadnikService.create('provider', $scope.employee);
        }

        if($scope.employee.type == 'CO') {
            RadnikService.create('provider', $scope.employee);
        }
        
    };
  
});

//kontroler za Providera
app.controller('ProviderController', function ($scope, $location, ProviderService) {

    $scope.create = function() {
         ProviderService.create('provider', $scope.provider); 
    };
  
});

app.controller('BasicUserController', function ($scope, BasicUserService) {

    $scope.registerSubmit = function(user) {
        if(user.password.localeCompare($scope.password2)) {
            BasicUserService.create(user).success(function(data){
                $scope.status = 'Uspesno';
            }).error(function(data){
                $scope.status = 'Neuspesno';
            });
        }
    }
});
