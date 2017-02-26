'use strict';

app.controller('BasicUserController', function ($scope, BasicUserService, AuthService) {

    $scope.registerSubmit = function(user) {
        if(user.password.localeCompare($scope.password2)) {
            BasicUserService.create(user).success(function(data){
                $scope.status = 'Uspesno';
            }).error(function(data){
                $scope.status = 'Neuspesno';
            });
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
        AuthService.logout();
    };

});

