<form method="post" action="{% url 'your_view_name' %}">  <!-- Replace 'your_view_name' -->
    {% csrf_token %}  <!-- This is essential -->
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <button type="submit">Register</button>
</form>