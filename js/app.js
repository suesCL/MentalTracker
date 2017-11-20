
var ViewModel = function(){
  var self = this;
  self.recordLevel = ko.observable();
	
	//a function for extract level value and send ajax request to backend 
	self.sendLevel = function(){
		$.ajax({
			type: "POST",
			url: "localhost:8000",
			data: self.recordLevel(),
			success: function(response){
				console.log(response);
			},
			error: function(error){
				alert("Data cannot be posted to backend.");
			}
		});

	};

var viewModel = new ViewModel();

ko.applyBindings(viewModel);