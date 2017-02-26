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