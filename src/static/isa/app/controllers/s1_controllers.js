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

app.controller('GuestController', function ($scope, $rootScope, $route, BasicUserService) {
    $scope.status = {};

    $scope.loadUser = function () {
            BasicUserService.getGuest($rootScope.currentUser.id).success(function (data) {
            $scope.user = data;
        });
    }

    $scope.loadUser();

    $scope.update = function() {
        BasicUserService.updateGuest($scope.user.id, $scope.user).success(function(data) {
            $scope.user = data;
            $scope.status.ok = true;
            $scope.status.fail = false;
        }).error(function(data){
            $scope.status.fail = true;
            $scope.status.ok = false;
            $scope.loadUser();
        });
    };

    $scope.reload = function() {
        $route.reload();
    };
});

