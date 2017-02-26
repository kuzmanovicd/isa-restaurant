'use strict';

app.factory('BasicUserService', BasicUserService);

app.factory('AuthService', AuthService);

function BasicUserService($http) {

    var service = {};

    service.create = create;

    return service;
    
    function create(link, provider) {
        console.log(provider);
        return $http.post('api/users/' + link + '/create/', angular.toJson(provider));
    }

    function create(data) {
        return $http.post('api/users/guests/create/', angular.toJson(data));
    }

}

function AuthService($http) {
    var service = {};
    service.Login = Login;
    service.SetCredentials = SetCredentials;
    service.ClearCredentials = ClearCredentials;
    service.Auth = Auth;
    service.Logout = Logout;
    service.Csrf = Csrf;

    return service;

    function Csrf(callback) {
        $http.get('api/users/csrf/').success(function (data) {
             callback(data);
        });
    }

    function Login(user, callback) {
        /* Use this for real authentication
         ----------------------------------------------*/
        console.log(angular.toJson(user));
        $http.post('api/users/auth/', angular.toJson(user))
            .success(function (response) {
                callback(response);
            });
    }

    function Auth(token, callback) {
        $http.post('api/users/verify/', angular.toJson(token)).success(function (data) {
            callback(data);
        });
    }

    function Logout(callback) {
        $http.get('api/users/logout').success(function (data) {
            callback(data);
        });
    }


    function SetCredentials(data) {
        $rootScope.currentUser = data.user;
        $http.defaults.headers.common['Authorization'] = 'JWT ' + data.token;
        $cookies.put('token', data.token);
    }

    function ClearCredentials() {
        $rootScope.currentUser = null;
        $http.defaults.headers.common['Authorization'] = "";
        $cookies.remove('token');
    }
}