$('#btn2').click(function() {$('input:checkbox').removeAttr('checked');
document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });});

//$('#chb2 input[type=checkbox]').prop('checked', false);
//$('#chb3 input[type=checkbox]').prop('checked', false);
//$('#chb1 input[type=checkbox]').prop('checked', false);

/* Установка состояний чекбоксов, после загрузки страницы */
(function() {
 'use strict';
 var cn = 'CheckBoxes', set = {}, cook = cookies(cn) || {};
 cookies.expires = 10 * 24 * 3600;

 function saveChecked() {
  cook[this.id] = this.checked;
  set[cn] = cook;

  // Записываем в кукис текущее значение checked
  cookies(set);
 };

 document.querySelectorAll('#chb1 input[type=checkbox]').forEach(function(i) {
  i.onchange = saveChecked;
  // Устанавливаем значение из кукиса
  i.checked = !!cook[i.id];
 })
document.querySelectorAll('#chb2 input[type=checkbox]').forEach(function(i) {
  i.onchange = saveChecked;
  // Устанавливаем значение из кукиса
  i.checked = !!cook[i.id];
 })
document.querySelectorAll('#chb3 input[type=checkbox]').forEach(function(i) {
  i.onchange = saveChecked;
  // Устанавливаем значение из кукиса
  i.checked = !!cook[i.id];
 })

})();


//var locations = [{% for value in spot_dict %}
//                [{{value[0]}}, {{value[1]}}, {{value[2]}}],
 //                {% endfor %}];
//                document.addEventListener('DOMContentLoaded', (event) => {
//                for (var i = 0; i < locations.length; i++) {marker = new L.marker([locations[i][1], locations[i][2]]).bindPopup(locations[i][0]).addTo(map);}});
