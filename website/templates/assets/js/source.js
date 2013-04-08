$(document).ready(function() {
	var numMines = 10; // number of mines the user still needs to place
	var placeMines = true; // whether or not the user has finished placing the mines
	var $opponentboard = $("#opponentboard"); 
	var $opponentlabel = $("#opponentlabel"); 
	var $userboard = $("#userboard");
	var $userlabel = $("#userlabel"); 
	
	/*
	 * Creates the user's tiles.
	 */
	function createTiles() {
		for(var i = 0; i < 100; i++) { // 100 tiles
			var button = document.createElement('input'); // create the button
			button.setAttribute('type','button');
			button.setAttribute('data-powerup','none');
			button.setAttribute('data-mine','false');
			button.setAttribute('id',"user"+i);
			button.className = "blank";
			button.onclick = function(){
				if(placeMines) {
					$this = $(this);
					if($this.attr('data-mine') == 'false') {
						if(numMines > 0) {
							numMines--;
							$this.toggleClass('mine blank');
							$this.attr('data-mine','true');
						} else {
							alert("You do not have any more mines to place!");
						}
					} else {
						numMines++;
						$this.toggleClass('mine blank');
						$this.attr('data-mine','false');
					}
					
					updateText();
				}
			};
			$userboard.append(button);
		}
	}
	
	function updateText() {
		$("#numberofmines").text("You have " + numMines + " mines left to place.");
	}
	
	/*
	 * Places three power-ups randomly on the user's board for the opponent to use.
	 */
	function placePowerups() {
		var powerups = ["immunity","health","ninesquares","opponenttwice","doubledamage","extramine","removemine","peek"];
		// we're putting three power-ups on the board
		for(var i = 0; i < 3; i++) {
			var powerupIndex = Math.floor(Math.random()*powerups.length); // pick random power-up
			var powerup = powerups[powerupIndex]; 
			powerups.splice(powerupIndex,1); // remove power-up from list
			var placedPowerup = false;
			while(!placedPowerup) { // keep looping until power-up is put on a free square
				$randomTile = $("#user" + Math.floor(Math.random()*100)); // pick a random tile
				// check tile's availability
				if($randomTile.attr("class") == "blank" && $randomTile.attr("data-powerup") == "none") {
					$randomTile.removeClass().addClass("powerup");
					$randomTile.attr("data-powerup",powerup);
					placedPowerup = true;
				}
			}
		}
	}
	$("#donebutton").click(function() {
		if(numMines > 0) {
			alert("You still have mines left to place!");
		} else {
			placeMines = false;
			$("#instructionarea").hide();
			$("#donearea").hide();
			placePowerups();
			$userlabel.show();
			setUpOpponentBoard();
		}
	});
	
	$("#findgamebutton").click(function() {
	//*
		$.ajax({
		datatype: "json",
		//username: "admin",
		//password: "awesomesauce",
		//crossDomain: "true",
		url: "http://netmines.herokuapp.com/game",
		type: "GET",
		data: {"player_one":"1", "player_two":"1", "current_board_state":"1", "mine_board_state":"1", "winner":"1", "turn":"1", "gamestatus":"1"},
		success: function(data){
		alert("success");
		},
		error: function(object) {
			var output = '';
			for (property in object) {
			  output += property + ': ' + object[property]+'\n';
			}
			console.log(output);
		}
	});//*/
	});
		
	
	function setUpOpponentBoard() {
		var url = ""; // fill in with the server url
		$opponentlabel.show();
		$opponentboard.show();
		//$opponentboard.load(url); // actual line to use
		$opponentboard.html($userboard.html()); // temporary just to fill something in
		$opponenttiles = $opponentboard.children();
		$.each($opponenttiles,function(){
			var $this = $(this);
			$this.attr("id",$this.attr("id").replace("user","opponent"))
			});
		$opponenttiles.removeClass().addClass("blank");
		$opponenttiles.click(function() {
			var $this = $(this);
			$this.removeClass();
			if($this.attr("data-mine") == "true") {
				$this.addClass("mine");
			} else if($this.attr("data-powerup") != "none") {
				$this.addClass("powerup");
			} else {
				$this.addClass("clickedblank");
			}
		});
	}
	
	$userlabel.hide();
	$userboard.hide();
	$opponentlabel.hide();
	$opponentboard.hide();
	$("#instructionarea").hide();
	$("#donearea").hide();
	createTiles();
	updateText();

});