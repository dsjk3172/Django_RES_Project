from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from users.models import User, Team


class UserRegisterViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.register_url = '/users/signup/'
        self.login_url = '/users/login/'
        
        self.team1 = Team.objects.create(name='단비')  # 테스트 팀
        self.team2 = Team.objects.create(name='다래')
        
        self.email = 'lee@naver.com'
        self.username = 'lee'
        self.pw = 'q1w2e3r4'
        self.user = User.objects.create_user(
            email=self.email,
            username=self.username,
            team=self.team1
        )
        self.user.set_password(self.pw)
        self.user.save()
    
    def test_default_values(self):
        """
        테스트 값 확인
        """
        assert self.user.email == 'lee@naver.com'
        assert self.user.username == 'lee'
        assert self.user.team == self.team1
        assert self.user.check_password('q1w2e3r4') == True
        assert self.user.is_active == True
        assert self.user.is_admin == False
        assert self.register_url == '/users/signup/'
        assert self.login_url == '/users/login/'
    
    def test_register(self):
        """
        회원가입 테스트
        """
        email = 'kim@naver.com'
        username = '김윙크'
        team = self.team2.id
        pw = '123456789!'
        
        data = {
            'email': email,
            'username': username,
            "team": team,
            'pw': pw
        }
        
        response = self.client.post(
            self.register_url,
            data=data,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['user']['email'] == email
        assert response.data['user']['username'] == username
        assert response.data['user']['team'] == team
        
    def test_login(self):
        """
        로그인 테스트
        """
        email = 'lee@naver.com'
        pw = 'q1w2e3r4'
        self.assertEqual(self.email, email)
        self.assertEqual(self.pw, pw)
        
        response = self.client.post(
            self.login_url,
            data={'email': email, 'pw': pw},
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['user']['email'] == email