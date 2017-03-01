'use strict';

app.controller('BasicUserController', function ($scope, $location, BasicUserService, AuthService) {

    $scope.loadUser = function () {
        BasicUserService.getGuest($rootScope.currentUser.id).success(function (data) {
            $scope.user = data;
        });
    }

    $scope.registerSubmit = function(user) {
        if(user.password == $scope.password2) {
            BasicUserService.createGuest(user).success( function(data){
                $scope.status = 'Uspesno';
                $location.path('/');
            }).error(function(data){
                $scope.status = 'Neuspesno';
            });
        } else {
            console.log('GRESKA PRI REGISTER SUBMIT');
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

app.controller('GuestController', function ($scope, $rootScope, $route, $location, BasicUserService, ReservationService, MenuService) {
    $scope.status = {};

    $scope.loadUser = function () {
        BasicUserService.getGuest($rootScope.currentUser.id).success(function (data) {
            $scope.user = data;
        });
    }

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

    $scope.loadInvites = function () {
        ReservationService.getInvites().success(function(data) {
            $scope.invites = data;
        });
    }

    $scope.confirmInvite = function(invite, confirm) {   
        var id = invite.id;
        var data = {};
        data.confirm = confirm;
        ReservationService.confirmInvite(id, data).success(function(data) {
            if(confirm) {
                $scope.order_waiting = true;
                $scope.order_invite_id = id;
                $scope.loadInvites();
                MenuService.get(invite.reservation.restaurant.restaurant_menu).success( function(data) {
                    $scope.menu = data;
                });

            } else {
                $scope.loadInvites();
            }
        });
    }

    $scope.order = function (selected) {
        var data = {};
        data.menu_items = [];
        for(var i = 0 ; i < selected.length; i++) {
            console.log(selected[i]);
            data.menu_items.push(selected[i]);
        }

        ReservationService.makeOrder($scope.order_invite_id, data).success(function(data){
            $scope.order_waiting = false;
        });
    }



    $scope.reload = function() {
        $route.reload();
    };

    $scope.getAllGuests = function () {
        console.log('pozvan getAllGuests');
        BasicUserService.getAllGuests().success(function(data){
            $scope.guests = data;
        });
    };

    $scope.getMyFriends = function () {
        console.log('pozvan getMyFriends');
        BasicUserService.getMyFriends().success(function(data){
            $scope.friends = data;
        });
    };

    $scope.getMyFriendsGuests = function () {
        console.log('pozvan getMyFriendsGuests');
        BasicUserService.getMyFriendsGuests().success(function(data){
            $scope.friends_guests = data;
        });
    };

    $scope.deleteFriend = function(friend) {
        console.log('pozvan deleteFrienship');
        BasicUserService.deleteFriend(friend).success(function(data) {
             $route.reload();
        });
    }

    $scope.deleteFriend2 = function(id) {
        console.log('pozvan deleteFrienship2');
        var friend;
        var i;
        for(i = 0; i < $scope.friends.length; i++) {
            if($scope.friends[i].to_user == id) {
                friend = $scope.friends[i];
                break;
            }
        }

        if(friend == null) {
            return;
        }


        BasicUserService.deleteFriend(friend).success(function(data) {
             $route.reload();
        });
    }

    $scope.addFriend = function (id) {
        var data = {
            "to_user": id
        }
        BasicUserService.addFriend(data).success( function(data) {
            $route.reload();
        });
    };

    $scope.isFriend = function(id) {
        var i = 0;
        for(i = 0; i < $scope.friends.length; i++) {
            if($scope.friends[i].to_user == id) {
                return true;
            }
        }
        return false;
    }

    //$scope.loadUser();

});

app.controller('ReservationController', function($scope, $rootScope, $location, ReservationService) {

    $scope.load = function () {
        ReservationService.myReservations().success(function(data){
            $scope.reservations = data;
        });
    }
});


