from jsonplaceholder_client import JsonPlaceholderClient, Post, Comment
from cat_api_client import CatAPIClient, CatImage
from email_verification_service import EmailVerificationService
from result_service import ResultService

# Инициализация клиентов и сервисов
jsonplaceholder_client = JsonPlaceholderClient()
cat_api_client = CatAPIClient()
email_verification_service = EmailVerificationService()
result_service = ResultService()

# Проверка е-мейла
email_to_verify = "test@example.com"
is_email_valid = email_verification_service.verify_email(email_to_verify)
print(f"\nEmail Verification Result for {email_to_verify}: {is_email_valid}")

# Получение всех постов
all_posts = jsonplaceholder_client.get_all_posts()
print("\nAll Posts:")
for post in all_posts:
    print(post.dict())

# Получение всех комментариев
all_comments = jsonplaceholder_client.get_all_comments()
print("\nAll Comments:")
for comment in all_comments:
    print(comment.dict())

# Получение случайного изображения кота
random_cat_image = cat_api_client.get_random_cat_image()
print("\nRandom Cat Image:")
print(random_cat_image.url)

# Сохранение результатов в сервисе
result_service.save_result({
    "posts": [post.dict() for post in all_posts],
    "comments": [comment.dict() for comment in all_comments],
    "cat_image_url": random_cat_image.url
})

# Получение всех сохраненных результатов
saved_results = result_service.get_all_results()
print("\nSaved Results:")
for result in saved_results:
    print(result)

# Получение всех подтвержденных е-мейлов
verified_emails = email_verification_service.get_verified_emails()
print("\nVerified Emails:")
print(verified_emails)

# Очистка подтвержденных е-мейлов
email_verification_service.clear_verified_emails()
print("\nVerified Emails after clearing:")
print(email_verification_service.get_verified_emails())
