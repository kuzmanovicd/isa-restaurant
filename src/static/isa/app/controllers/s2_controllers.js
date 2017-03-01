'use strict';

app.controller('RestaurantController', function ($scope, $rootScope, $location, $routeParams, $route, RestaurantService, BasicUserService, TableService, MenuService, ReservationService, RadnikService, ShiftService) {

    RestaurantService.get($routeParams.id).success(function(data) {
        $scope.restaurant = data;
    });

    //dodavanje providera
    $scope.addProvider = function() {
        console.log('addProvider');
        $location.path('/provider/add');
    };

    //dodavanje randika
    $scope.addRadnik = function() {
        console.log('addRadnik');
        $location.path('/employee/add');
    };

    //dodavanje regiona
     $scope.addRegion = function() {
        console.log('addRegion');
        $location.path('/region/add');
    };

    //dodaj menu item
    //dodavanje regiona
     $scope.addMenuItem = function() {
        $location.path('/menu_item/add');
    };


    //pogledaj meni
    $scope.openMenu = function(id) {
        $location.path('/menu/open/' + id);
    };

    //za radnike
    $scope.izlistajRadnika = function(id) {
        $location.path('/employee/open/' + id)
    }

    //za smenu
    $scope.addShift = function() {
        $location.path('/shift/add');
    };

    $scope.getAll = function() {
        RestaurantService.getAll().success(function (data) {
            $scope.restaurants = data;
        });
    };

    if($rootScope.currentUser && $rootScope.currentUser.user_type == 'RM') {
        BasicUserService.getRestaurantManager($rootScope.currentUser.id).success(function (data) {
            RestaurantService.get(data.working_in).success(function(data) {
                $scope.restaurant = data;
                $scope.getRegions(data.id);

                //$scope.getMenus(data.id);
            });
        });
    } else {
    }


    $scope.getRegions = function(id) {

        if(id == undefined) {
            id = $routeParams.id;
        }

        TableService.getRegions(id).success(function(data) {
           $scope.regions = data;
        });
    }

    $scope.getFriends = function() {
        BasicUserService.getMyFriendsGuests().success(function(data){
            $scope.friends = data;
        });
    };

    //dejan
    $scope.selected = [];
    $scope.todayDate = new Date();
    //$scope.nowTime = new Time

    $scope.reserve = function (r) {
        var index = -1;
        for(var i = 0; i < $scope.selected.length; i++) {
            if($scope.selected[i].id == r.id) {
                index = i;
                break;
            }
        }

        if(index == -1) {
            $scope.selected.push(r);
            r.selected = true;
        } else {
            $scope.selected.splice(index, 1);
            r.selected = false;
        }
        
    };

    $scope.createReservation = function (data) {
        var d = new Date(data.coming);
        data.coming = d.toISOString();
        data.restaurant = $scope.restaurant.id;
        data.reserved_tables = [];

        for(var i = 0; i < $scope.selected.length; i++) {
            data.reserved_tables.push($scope.selected[i].id);
        }
        console.log(data);

        ReservationService.create(data).success(function(data){
            console.log(data);
            var invite = {};
            invite.guests = $scope.selected.friends;
            invite.reservation = data.id;
            console.log(invite);
            //return;
            if($scope.selected.invite) {
                ReservationService.sendInvites(invite).success(function(data) {
                    $scope.ok = true;
                    $scope.error = false;
                });
            } else {
                $scope.ok = true;
                $scope.error = false;
            }
            
        }).error(function(data){
            $scope.error = true;
            $scope.ok = false;
        });
    };


});


//kontroler za radnika
app.controller('RadnikController', function ($scope, $routeParams, RadnikService, TableService, ShiftService) {
    //WA - Waiter
    //BA - Bartender
    //C0 - Cook
    $scope.employee_types = ['WA', 'BA', 'CO'];

    $scope.create = function() {
        if($scope.employee.type == 'WA') {
            RadnikService.create('waiter', $scope.employee);
        }

        if($scope.employee.type == 'BA') {
            RadnikService.create('bartender', $scope.employee);
        }

        if($scope.employee.type == 'CO') {
            RadnikService.create('cook', $scope.employee);
        }
        
    };

    $scope.get = function() {
        RadnikService.get($routeParams.id).success( function(data) {
            $scope.employee = data;
        });
    }

    $scope.getRegions = function() {
        TableService.getRegions($routeParams.id).success(function(data) {
           $scope.regions = data;
        });
    }


     $scope.getAllEmployees = function () {
        $scope.get();
        $scope.getRegions();
        $scope.getAllShifts();
    };

    $scope.updateRegion = function(m) {
        var data = {};
        data.region = m.updated_region;
        RadnikService.update(m.id, data).success(function(data){
            //$scope.regions = data;
            $scope.getAllEmployees();
        })
    };

    $scope.updateShift = function(m) {
        var data = {};
        data.shift = m.updated_shift;
        RadnikService.update(m.id, data).success(function(data){
            //$scope.regions = data;
            $scope.getAllEmployees();
        })
    };

    $scope.getAllShifts = function() {
        ShiftService.get().success(function(data) {
            $scope.shifts = data;
        })
    };

});

//kontroler za Providera
app.controller('ProviderController', function ($scope, $location, $rootScope, ProviderService) {

    $scope.update = function() {
        ProviderService.updateProvider($scope.user.id, $scope.user).success(function(data) {
            $scope.user = data;
            $scope.status.ok = true;
            $scope.status.fail = false;
        }).error(function(data){
            $scope.status.fail = true;
            $scope.status.ok = false;
            $scope.loadProvider();
        });
    };

    $scope.create = function() {
         //$scope.user.restaurant = -1;
         console.log($scope.provider)
         ProviderService.create($scope.provider).success(function(data) {
             //$location.path('/');
             window.history.back();
         }); 
    };

    $scope.loadProvider = function () {
        ProviderService.getProvider($rootScope.currentUser.id).success(function (data) {
            $scope.user = data;
        });
    };

  
});


//kontroler za stolove
app.controller('TableController', function($scope, TableService){
    $scope.getRegions = function() {
        var id;
        console.log('id2 je  ' + $scope.$parent.restaurant);
        console.log('id2 je  ' + $scope.$parent.$parent.restaurant);
        TableService.getRegions(id).success(function(data) {
           $scope.regions = data;
        });
    }

    //dejan
    $scope.selected = [];
    $scope.todayDate = new Date();
    //$scope.nowTime = new Time

    $scope.reserve = function (r) {
        var index = -1;
        for(var i = 0; i < $scope.selected.length; i++) {
            if($scope.selected[i].id == r.id) {
                index = i;
                break;
            }
        }

        if(index == -1) {
            $scope.selected.push(r);
            r.selected = true;
        } else {
            $scope.selected.splice(index, 1);
            r.selected = false;
        }
        
    };

})



//kontroler za Region
app.controller('RegionController', function ($scope, $location, RegionService) {

    $scope.region = {};
    $scope.region.is_open = false;
    $scope.region.is_forSmoke = false;

    $scope.create = function() {
        $scope.region.is_frontSide = true;
        console.log($scope.region);
        RegionService.create($scope.region).success(function(data) {
            //$location.path('/');
            window.history.back();
        }); 
    };

    //console.log(angular.toJson(region));
  
});


//kontroler za menu
app.controller('MenuController', function ($scope, $rootScope, $location, $routeParams, MenuService, OfferService) {

    $scope.create = function() {
        MenuService.create($scope.menu).success(function(data) {
            $location.path('/');
        }); 
    };

    $scope.getAllMenuItems = function () {
        console.log('aaaaaaa')
        $scope.get();
    };

    $scope.get = function() {
        MenuService.get($routeParams.id).success( function(data) {
            $scope.menu = data;
        });
    };

    $scope.deleteMenuItem = function(id) {
        MenuService.destroy(id).success(function(data) {
            $scope.get();
        });
    };

    $scope.addMenuItem = function(data) {
        data.menu = $scope.menu.id;
        $scope.return = data;
        MenuService.addItem(data).success(function(data) {
            $scope.get();
        });
    };

    $scope.sendOrder  = function(data) {
        var items = $scope.menu.menu_items;
        var data = {};
        data.items = [];
        //data.quantity = [];
        data.restaurant = $scope.menu.restaurant;
        for(var i = 0; i < items.length; i++) {
            if(items[i].order_quantity) {
                var item = {};
                item.id = items[i].id;
                item.quantity = items[i].order_quantity;
                data.items.push(item);
            }
        }
        $scope.data2 = data;

        OfferService.create(data).success(function(data) {
            console.log('uspesno');
        });
    }


});


//kontroler za smenu
app.controller('ShiftController', function ($scope, $location, $routeParams, ShiftService) {

    $scope.create = function() {
        ShiftService.create($scope.shift).success(function(data) {
            //$location.path('/');
        }); 
    };
});


//kontroler za itemsRequest
app.controller('ItemsRequestController', function ($scope, $location, $routeParams, ItemsRequestService) {


      $scope.create = function() {
        MenuService.create($scope.menu).success(function(data) {
            $location.path('/');
        }); 
    };

    
});


