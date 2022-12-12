import graphene
from graphene_django import DjangoObjectType
from .models import BookCategory, Book, Order, Client


class BookCategoryType(DjangoObjectType):
    class Meta:
        model = BookCategory
        fields = ('id', 'name')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'book_category',
            'publication_date',
            'added_time',
            'author',
        )


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'gender',
            'address',
            'birthdate',
            'added_time',
        )

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = (
            'id',
            'client',
            'book',
            'price',
            'quantity',
        )


class Query(graphene.ObjectType):
    categories = graphene.List(BookCategoryType)
    books = graphene.List(BookType)
    clients = graphene.List(ClientType)
    orders = graphene.List(OrderType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return BookCategory.objects.all()

    def resolve_clients(root, info, **kwargs):
        # Querying a list
        return Client.objects.all()

    def resolve_orders(root, info, **kwargs):
        # Querying a list
        return Order.objects.all()


class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category
        name = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(BookCategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = BookCategory.objects.get(pk=id)
        category.name = name
        category.save()

        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        name = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(BookCategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = BookCategory()
        category.name = name
        category.save()

        return CreateCategory(category=category)


class BookInput(graphene.InputObjectType):
    title = graphene.String()
    book_category = graphene.String()
    publication_date = graphene.Date()
    added_time = graphene.DateTime()
    author = graphene.String()


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.book_category = input.book_category
        book.publication_date = input.publication_date
        book.added_time = input.added_time
        book.author = input.author
        book.save()
        return CreateBook(book=book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.title = input.title
        book.publication_date = input.publication_date
        book.added_time = input.added_time
        book.author = input.author
        book.save()
        return UpdateBook(book=book)


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)