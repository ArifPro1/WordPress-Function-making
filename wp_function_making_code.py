import wp_func

first_p_text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum"

heading_one_text = "Why do we use it ?"

second_p_text = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable."

article = wp_func.wp_p(first_p_text)+wp_func.h2(heading_one_text)+wp_func.wp_p(second_p_text)
print(article)
