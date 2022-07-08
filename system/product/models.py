from django.db import models


class BbCategoriesImport(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    detailid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'bb_categories_import'

        def __str__(self):
            fila = "Producid: " + self.productid + "Detailid: " + self.detailid + "Name: " + self.name
            return fila




class BbDetailsImport(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bb_details_import'


class BbProductImages(models.Model):
    productid = models.IntegerField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    href = models.TextField(blank=True, null=True)
    s3ref = models.TextField(blank=True, null=True)
    primaryimage = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bb_product_images'


class BbProductImport(models.Model):
    addtocarturl = models.TextField(blank=True, null=True)
    bestsellingrank = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    customerreviewaverage = models.FloatField(blank=True, null=True)
    customerreviewcount = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dollarsavings = models.TextField(blank=True, null=True)  # This field type is a guess.
    features = models.TextField(blank=True, null=True)  # This field type is a guess.
    freeshipping = models.BooleanField(blank=True, null=True)
    includeditems = models.TextField(blank=True, null=True)  # This field type is a guess.
    instoreavailability = models.BooleanField(blank=True, null=True)
    instoreavailabilitytext = models.TextField(blank=True, null=True)
    longdescription = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    mobileurl = models.TextField(blank=True, null=True)
    modelnumber = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    onlineavailability = models.BooleanField(blank=True, null=True)
    onlineavailabilitytext = models.TextField(blank=True, null=True)
    onsale = models.BooleanField(blank=True, null=True)
    preowned = models.BooleanField(blank=True, null=True)
    regularprice = models.TextField(blank=True, null=True)  # This field type is a guess.
    saleprice = models.TextField(blank=True, null=True)  # This field type is a guess.
    shippingcost = models.TextField(blank=True, null=True)  # This field type is a guess.
    shortdescription = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)
    thumbnailimage = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    upc = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bb_product_import'


class Databasechangelog(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    author = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    dateexecuted = models.DateTimeField()
    orderexecuted = models.IntegerField()
    exectype = models.CharField(max_length=10)
    md5sum = models.CharField(max_length=35, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    liquibase = models.CharField(max_length=20, blank=True, null=True)
    contexts = models.CharField(max_length=255, blank=True, null=True)
    labels = models.CharField(max_length=255, blank=True, null=True)
    deployment_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangelog'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(blank=True, null=True)
    lockedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'

  