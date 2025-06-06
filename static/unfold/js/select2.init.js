"use strict";
{
  const $ = django.jQuery;

  $.fn.djangoCustomSelect2 = function () {
    $.each(this, function (i, element) {
      if (element.id.match(/__prefix__/)) {
        return;
      }

      $(element).select2();
    });

    return this;
  };

  $.fn.djangoAdminSelect2 = function () {
    $.each(this, function (i, element) {
      $(element).select2({
        ajax: {
          data: (params) => {
            return {
              term: params.term,
              page: params.page,
              app_label: element.dataset.appLabel,
              model_name: element.dataset.modelName,
              field_name: element.dataset.fieldName,
            };
          },
        },
      });
    });
    return this;
  };


  document.addEventListener("formset:added", (event) => {
    $(event.target).find(".admin-autocomplete").djangoAdminSelect2();
  });
}
