from django.db import models

# Create your models here.
class Word(models.Model):
	word= models.CharField(max_length=30)
	
	def __unicode__(self):
		return '%s' % self.word


class Language(models.Model):
	designation= models.CharField(max_length=30)
	words = models.ManyToManyField(Word)
	
	def __unicode__(self):
		return '%s' % self.designation
        
        
class Contain(models.Model):
    language = models.ForeignKey(Language)
    word = models.ForeignKey(Word)
    

class TypeOfWord(models.Model):
	designation= models.CharField(max_length=30)
	words= models.ForeignKey(Contain)
	
	def __unicode__(self):
		return '%s' % self.designation
  
    
class WordType(models.Model):
	word= models.ForeignKey(Contain)
	type= models.ForeignKey(TypeOfWord)
	
	phonetic = models.CharField(max_length=60)


class Meaning(models.Model):
	word= models.ForeignKey(WordType)
	meaning=models.CharField(max_length=1000)
