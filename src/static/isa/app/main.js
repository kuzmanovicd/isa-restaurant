'use strict';

var app = angular.module('mainApp', ['ngRoute', 'ngCookies']).run(run);

app.config(function ($routeProvider) {

    var static_file = 'static/isa/';
    $routeProvider
        .when('/home', {
            template: '<h1>Homepage</h1>'
        })
        .when('/login', {
            controller: 'BasicUserController',
            templateUrl: static_file + 'partials/student1/login.html',
            controllerAs: 'vm'
        })
        .when('/register', {
            controller: 'BasicUserController',
            templateUrl: static_file + 'partials/student1/register.html',
            controllerAs: 'vm'
        })
        .when('/restaurant/:id', {
            controller: 'RestaurantController',
            templateUrl: static_file + 'partials/student2_restoran/profil_restorana.html',
            controllerAs: 'vm'
        })
        .when('/restaurant', {
            controller: 'RestaurantController',
            templateUrl: static_file + 'partials/student2_restoran/profil_restorana.html',
            controllerAs: 'vm'
        })
        .when('/restaurants', {
            controller: 'AllRestaurantsController',
            templateUrl: static_file + 'partials/student1/restaurants.html',
            controllerAs: 'vm'
        })
        .when('/guest', {
            controller: 'GuestController',
            templateUrl: static_file + 'partials/student1/guest_profile.html',
            controllerAs: 'vm'
        })
        .when('/guests', {
            controller: 'GuestController',
            templateUrl: static_file + 'partials/student1/guest_list.html',
            controllerAs: 'vm'
        })
        .when('/provider/add', {
            controller: 'ProviderController',
            templateUrl: static_file + 'partials/student2_restoran/provider_add.html',
            controllerAs: 'vm'
        })
        .when('/provider', {
            controller: 'ProviderController',
            templateUrl: static_file + 'partials/student2_restoran/profil_provider.html',
            controllerAs: 'vm'
        })
        .when('/menu_item/add', {
            controller: 'ProviderController',
            templateUrl: static_file + 'partials/student2_restoran/menu_item_add.html',
            controllerAs: 'vm'
        })
        .when('/employee/add', {
            controller: 'RadnikController',
            templateUrl: static_file + 'partials/student2_restoran/radnik_add.html',
            controllerAs: 'vm'
        })
        .when('/region/add', {
            controller: 'RegionController',
            templateUrl: static_file + 'partials/student2_restoran/region_add.html',
            controllerAs: 'vm'
        })
        .when('/employee/open/:id', {
            controller: 'RadnikController',
            templateUrl: static_file + 'partials/student2_restoran/lista_radnika.html',
            controllerAs: 'vm'
        })
        .when('/menu/open/:id', {
            controller: 'MenuController',
            templateUrl: static_file + 'partials/student2_restoran/pogledaj_meni.html',
            controllerAs: 'vm'
        })
        .when('/menu/naruci/:id', {
            controller: 'MenuController',
            templateUrl: static_file + 'partials/student1/naruci.html',
            controllerAs: 'vm'
        })
        .when('/proizvodi', {
            controller: 'productsController',
            templateUrl: static_file + 'partials/product.html',
            controllerAs: 'vm'
        })
        .when('/proizvod', {
            controller: 'productsController',
            templateUrl: static_file + 'partials/productinfo.html',
            controllerAs: 'vm'
        })
        .when('/proizvod/dodaj', {
            controller: 'productsController',
            templateUrl: static_file + 'partials/proizvod_add.html',
            controllerAs: 'vm'
        })
        .when('/proizvod/izmena', {
            controller: 'productsController',
            templateUrl: static_file + 'partials/proizvod_edit.html',
            controllerAs: 'vm'
        })
        .when('/prodavnice', {
            controller: 'StoreController',
            templateUrl: static_file + 'partials/store.html',
            controllerAs: 'vm'
        })
        .when('/prodavnica/dodaj', {
            controller: 'StoreController',
            templateUrl: static_file + 'partials/prodavnica_add.html',
            controllerAs: 'vm'
        })
        .when('/prodavnica/izmena', {
            controller: 'StoreController',
            templateUrl: static_file + 'partials/prodavnica_edit.html',
            controllerAs: 'vm'
        })
        .when('/kategorija/dodaj', {
            controller: 'ProductCategoryController',
            templateUrl: static_file + 'partials/kategorija_add.html'
        })
        .when('/kategorija/izmena', {
            controller: 'ProductCategoryController',
            templateUrl: static_file + 'partials/kategorija_edit.html'
        })
        .when('/dostavljac/dodaj', {
            controller: 'DostavljacController',
            templateUrl: static_file + 'partials/dostavljac_add.html'
        })
        .when('/dostavljac/izmena', {
            controller: 'DostavljacController',
            templateUrl: static_file + 'partials/dostavljac_edit.html'
        })
        .when('/recenzija/izmena', {
            controller: 'RecenzijaController',
            templateUrl: static_file + 'partials/recenzija_edit.html'
        })
        .when('/akcija/dodaj', {
            controller: 'AkcijaController',
            templateUrl: static_file + 'partials/akcija_add.html'
        })
        .when('/korpa', {
            //controller: 'storeController',
            templateUrl: static_file + 'partials/cart.html'
        })
        .when('/menadzment', {
            controller: 'AkcijaController',
            templateUrl: static_file + 'partials/menadzment.html'
        })
        .when('/admin', {
            //controller: 'storeController',
            templateUrl: static_file + 'partials/admin_panel.html'
        })
        .when('/zalba', {
            controller: 'KupovinaController',
            templateUrl: static_file + 'partials/zalba_add.html'
        })
        .when('/istorijakupovine', {
            //controller: 'storeController',
            templateUrl: static_file + 'partials/istorija_kupovine.html'
        })
        .when('/listazelja', {
            controller: 'WishListController',
            templateUrl: static_file + 'partials/listazelja.html'
        })
        .when('/welcome', {
            resolve: {
                "check": function ($location, $rootScope) {
                    if (!$rootScope.currentUser) {
                        $location.path('/login');
                    }
                }
            },
            template: '<h1>Logged In</h1>'
        })
        .otherwise({
            redirectTo: '/home'
        })

});

function run($rootScope, $location, $cookieStore, $cookies, $http, AuthService, ShoppingCartService) {

    AuthService.Csrf(function(data) {
        
    });

    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    if($cookies.get("token")) {
        $http.defaults.headers.common['Authorization'] = "JWT " + $cookies.get("token");
    } else {
        $http.defaults.headers.common['Authorization'] = "";
    }
    
    var d = { "token": $cookies.get("token")};  

    AuthService.Auth(d, function (data) {
        if (data.user.username) {
            console.log("Auth in run: " + data);
            AuthService.SetCredentials(data);
            ShoppingCartService.getCartCount().success(function (data) {
                if (data) {
                    $rootScope.cartCount = data;
                }
            });

            console.log('auth set credentials ' + $rootScope.currentUser)
        } else {
            AuthService.ClearCredentials();
        }
        changeLocation();
    });
    
    function changeLocation() {
        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a
            // restricted page
            var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            if (restrictedPage && !$rootScope.currentUser) {
                //console.log("locationChange in run");
                $location.path('/login');
            }
        });
    }

}
