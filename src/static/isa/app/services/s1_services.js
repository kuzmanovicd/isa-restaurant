'use strict';

app.factory('BasicUserService', BasicUserService);

app.factory('AuthService', AuthService);

app.factory('ReservationService', ReservationService);

app.factory('OfferService', OfferService);

function BasicUserService($http) {

    var service = {};

    service.createGuest = createGuest;
    service.getGuest = getGuest;
    service.updateGuest = updateGuest;
    service.addFriend = addFriend;
    service.deleteFriend = deleteFriend;
    service.getMyFriends = getMyFriends;
    service.getMyFriendsGuests = getMyFriendsGuests;
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

    function getMyFriendsGuests() {
        return $http.get('api/users/friends/guests/');
    }

    function addFriend(data) {
        return $http.post('api/users/friends/', angular.toJson(data));
    }

    function deleteFriend(data) {
        return $http.post('api/users/friends/delete/', angular.toJson(data));
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

function ReservationService($http) {
    var service = {};

    service.create = create;
    service.sendInvites = sendInvites;
    service.getInvites = getInvites;
    service.confirmInvite = confirmInvite;
    service.makeOrder = makeOrder;
    service.myReservations = myReservations;
    service.cancelReservation = cancelReservation;

    return service;

    function create(data) {
        return $http.post('api/restaurant/reservations/create/', angular.toJson(data));
    }

    function sendInvites(data) {
        return $http.post('api/restaurant/reservations/invite/create/', angular.toJson(data));
    }

    function getInvites() {
        return $http.get('api/restaurant/reservations/invite/my/');
    }

    function confirmInvite(id, data) {
        return $http.post('api/restaurant/reservations/invite/confirm/' + id + '/', angular.toJson(data));
    }

    function makeOrder(id, data) {
        return $http.post('api/restaurant/reservations/make-order/' + id + '/', angular.toJson(data));
    }

    function myReservations() {
        return $http.get('api/restaurant/reservations/my/');
    }

    function cancelReservation(id) {
        return $http.get('api/restaurant/reservations/cancel/' + id + '/');
    }

    
}

function OfferService($http) {

    var service = {};

    service.create = create;

    return service;

    function create(data) {
        return $http.post('api/restaurant/itemsrequest/create/', angular.toJson(data));
    }

}