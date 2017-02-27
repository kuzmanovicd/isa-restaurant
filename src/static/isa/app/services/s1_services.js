'use strict';

app.factory('BasicUserService', BasicUserService);

app.factory('AuthService', AuthService);

function BasicUserService($http) {

    var service = {};

    service.createGuest = createGuest;
    service.getGuest = getGuest;
    service.updateGuest = updateGuest;
    service.addFriend = addFriend;
    service.getMyFriends = getMyFriends;
    service.createRestaurantManager = createRestaurantManager;
    service.getRestaurantManager = getRestaurantManager;
    service.getAllGuests = getAllGuests;
    service.getAllRestaurantManagers = getAllRestaurantManagers;

    return service;

    function createGuest(data) {
        return $http.post('api/users/guests/create/', angular.toJson(data));
    }

    function getGuest(id) {
        return $http.get('api/users/guests/' + id);
    }

    function updateGuest(id, data) {
        return $http.patch('api/users/guests/' + id + '/', angular.toJson(data));
    }

    function getAllGuests() {
        return $http.get('api/users/guests/all/');
    }

    function getMyFriends() {
        return $http.get('api/users/friends/my/');
    }

    function addFriend(data) {
        return $http.post('api/users/friends/add/', angular.toJson(data));
    }

    function createRestaurantManager(data) {
        return $http.post('api/users/restaurant_manager/create/', angular.toJson(data));
    }

    function getRestaurantManager(id) {
        return $http.get('api/users/restaurant_manager/' + id);
    }

    function getAllRestaurantManagers() {
        return $http.get('api/users/restaurant_manager/all/');
    }

}

function AuthService($http, $rootScope, $cookies, $location) {
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
        }).error(function(data) {
            console.log(data);
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
        $location.path('/');
    }
}
