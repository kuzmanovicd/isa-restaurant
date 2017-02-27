'use strict';

app.controller('BasicUserController', function ($scope, $location, BasicUserService, AuthService) {


    $scope.registerSubmit = function(user) {
        
        if(user.password == $scope.password2) {
            BasicUserService.createGuest(user).success(function(data){
                $scope.status = 'Uspesno';
            }).error(function(data){
                $scope.status = 'Neuspesno';
            });
        } else {

        }
    }

    $scope.loginSubmit = function () {
        $scope.dataLoading = true;
        AuthService.Login($scope.user, function (data) {
            if (data.user.username) {
                AuthService.SetCredentials(data);
                $location.path('/');
            } else {
                $scope.dataLoading = false;
            }
        });
    }

    $scope.logout = function () {
        AuthService.ClearCredentials();
    };

});

app.controller('AllRestaurantsController', function ($scope, $location, RestaurantService, BasicUserService) {
    
    RestaurantService.getAll().success(function (data) {
        $scope.restaurants = data;
    });

});

app.controller('MyRestaurantController', function ($scope, $rootScope, BasicUserService, RestaurantService) {
    if($rootScope.currentUser.user_type == 'RM') {
        BasicUserService.getRestaurantManager($rootScope.currentUser.id).success(function (data) {
            RestaurantService.get(data.working_in).success(function(data) {
                $scope.restaurant = data;
            });
        });
    }
});
