 $("#id_country").change(function () {
      var url = $("#workerForm").attr("data-cities-url");
      var countryId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'country': countryId
        },
        success: function (data) {
          $("#id_city").html(data);
        }
      });

    });

 $("#id_category").change(function () {
      var url = $("#workerForm").attr("data-subcategory-url");
      var categoryId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'category': categoryId
        },
        success: function (data) {
          $("#id_subcategory").html(data);
        }
      });

    });