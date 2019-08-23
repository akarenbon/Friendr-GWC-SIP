
<?php
if(isset($_POST['add_friend'])) {
$current_user = $_SESSION['user_id']; //This will fetch user id of the person who is logged in and for this you need to have a user id in your session for the user who logs in

$friendid = $_POST['friend_id']; //This will assign friend id to variable $friendid

$_SESSION['user_id'] = //loggedin user id

//Now execute the insert statement
if(mysqli_query($connect, "INSERT INTO addfriendtable(user_id, friend_id) VALUES('$current_user','$friendid')")) {
echo 'success';
} else {
echo 'Error Occured';
}
}

$fetch_records = mysqli_fetch_array($connect, "SELECT name, userid FROM table");
while ($show_users = mysqli_fetch_array($fetch_records)) {
//loop all search results
//place this code in front of all results
?>
<form method="post">
<input type="hidden" value="<?php echo $show_users['user_id']; ?>" name="friend_id">
<input type="submit" name="add_friend" value="Add Friend" />
</form>
<?php
}
?>
