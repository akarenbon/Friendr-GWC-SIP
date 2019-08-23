$('.add-btn').click(() => {
  $('.two').addClass('in');
  $('.add-text').addClass('out');
  $('.text').addClass('move').html('Friends');
  $('.plus').addClass('tick');

  setTimeout(() => {
    $('.two').removeClass('in');
    $('.add-text').removeClass('out');
    $('.text').removeClass('move').html('Add Friend');
    $('.plus').removeClass('tick');
  }, 5000);
});
