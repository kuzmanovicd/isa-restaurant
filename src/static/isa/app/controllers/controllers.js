'use strict';

app.controller('RestaurantController', function ($scope, RestaurantService) {
    
    RestaurantService.get(1).success(function(data) {
        //console.log(data);
        $scope.restaurant = data;
    });
});