(function (document, window, $, Backbone, _){
	

	UTT.Routers.AppRouter = Backbone.Router.extend({

		routes: {
			"" 	: "home", 
			"userlist" : "registerUsers", 
			"meetrequests" : "createRequests"
		},

		initialize : function(){
			console.log("initialize");					

		},

		home : function(){			
			this.home = new UTT.Views.Home();				
			$("#content").html(this.home.el);
			// this.authen.selectMenuItem('applications');				
		},

		registerUsers : function(){			
			this.home = new UTT.Views.User();				
			$("#content").html(this.home.el);
			// this.authen.selectMenuItem('applications');				
		}, 

		createRequests : function(){			
			this.home = new UTT.Views.Request();				
			$("#content").html(this.home.el);
			// this.authen.selectMenuItem('applications');				
		}

	});

	UTT.templateLoader.load(["Home", "Restaurant", "User", "UserList", "Request", "RequestList"],function () {      
		$(document).ready(function(){
			app = new UTT.Routers.AppRouter();
			Backbone.history.start();
		});
	});


}(document, this, jQuery, Backbone, _));
