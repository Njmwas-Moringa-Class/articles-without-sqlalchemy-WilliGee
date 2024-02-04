#!/usr/bin/env python3
import sys
sys.path.append('lib')

import ipdb;

from Author import Author
from Magazine import Magazine
from Article import Article


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    
    author1 = Author("Richard Wall")
    author2 = Author("Cherie Smith")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("Just For Now")
    magazine2 = Magazine("The Song Bird")


    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "The Postman")
    article2 = author1.add_article(magazine1, "Drunkness at Work")
    article3 = author2.add_article(magazine2, "Sing a Song")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")


# DO NOT REMOVE THIS
    ipdb.set_trace()
