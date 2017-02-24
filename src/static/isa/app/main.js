'use strict';

var app = angular.module('mainApp', ['ngRoute', 'ngCookies']).run(run);

app.config(function ($routeProvider) {

    var static_file = 'static/isa/';
    $routeProvider
        .when('/home', {
            template: '<h1>Homepage</h1>'
        })
        .when('/login', {
            controller: 'loginController',
            templateUrl: static_file + 'partials/login.html',
            controllerAs: 'vm'
        })
        .when('/register', {
            controller: 'registerController',
            templateUrl: static_file + 'partials/register.html',
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

function run($rootScope, $location, $cookieStore, $http, AuthenticationService, ShoppingCartService) {
    /*
    var user = {};
    user.korisnickoime = 'dejan';
    user.password = 'hehehe';
    user.role = 'ADMIN';
    AuthenticationService.SetCredentials(user);
    changeLocation();
    */
    
    AuthenticationService.Auth(function (data) {
        // console.log(data);
        return;

        if (data.username) {
            console.log("Auth in run: " + data);
            AuthenticationService.SetCredentials(data);
            ShoppingCartService.getCartCount().success(function (data) {
                if (data) {
                    $rootScope.cartCount = data;
                }
            });

            console.log('auth set credentials ' + $rootScope.currentUser)
        } else {
            AuthenticationService.ClearCredentials();
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
