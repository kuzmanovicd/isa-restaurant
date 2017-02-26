'use strict';

app.controller('RestaurantController', function ($scope, RestaurantService) {
    
    RestaurantService.get(1).success(function(data) {
        //console.log(data);
        $scope.restaurant = data;
    });
});


app.controller('RadnikController', function ($scope, RadnikService) {

    $scope.employee_types = ['WA', 'BA', 'CO'];

    $scope.create = function() {
        if($scope.employee.type == 'WA') {
            RadnikService.create('provider', $scope.employee);
        }
        
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