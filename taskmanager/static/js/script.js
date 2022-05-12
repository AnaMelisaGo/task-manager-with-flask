document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "mmm dd, yyyy",
      i18n: {done: "Select"},
      autoClose: "true"
    });

    // select initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    // collapsible initialization
    let collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse);
});
