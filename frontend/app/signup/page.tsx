'use client';

import { useState } from 'react'; // 입력을 기억하기 위한 상태 관리가 필요해요.
import { useRouter } from 'next/navigation';

export default function SignupPage() {
  const router = useRouter();

  // 1. 입력값을 저장할 바구니(State)를 만들어요.
  const [formData, setFormData] = useState({
    user_id: '',
    user_pw: '',
    user_name: ''
  });

  // 2. 입력창에 글자를 칠 때마다 바구니에 업데이트하는 함수예요.
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  // 3. 가입 버튼을 눌렀을 때 실행되는 함수예요. (ViewSet API 호출)
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // 페이지가 새로고침되는 것을 막아요.

    try {
      // 새로운 ViewSet 주소로 데이터를 보내요.
      const response = await fetch('http://localhost:8000/api/v1/members/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData), // JSON 형식으로 변환해서 보내요.
      });

      const result = await response.json();

      if (response.ok) {
        // 성공 시: 백엔드에서 보낸 메시지와 DB 정보를 알림창으로 띄워요.
        let successMsg = `[가입 완료]\n`;
        Object.entries(result).forEach(([key, value]) => {
          successMsg += `${key} : ${value}\n`;
        });
        alert(successMsg);
        
        // 가입 성공 후 입력창을 비워주거나 로그인 페이지로 보낼 수 있어요.
        router.push('/login'); 
      } else {
        // 실패 시: 중복 아이디 등 에러 메시지를 띄워요.
        console.log("콘솔에 찍어보고 있다.", result.message);
        alert(`[에러 발생]\n메시지: ${result.message || '가입에 실패했습니다.'}`);
      }
    } catch (error) {
      console.error('통신 에러:', error);
      alert('서버와 연결할 수 없습니다.');
    }
  };

  return (
    <div style={containerStyle}>
      {/* 이제 action과 method 대신 onSubmit을 사용해요. */}
      <form style={cardStyle} onSubmit={handleSubmit}>
        <h2 style={titleStyle}>회원가입</h2>

        <div style={inputGroupStyle}>
          <label htmlFor="userid" style={labelStyle}>아이디</label>
          <input 
            type="text" 
            id="userid" 
            name="user_id" 
            style={inputStyle} 
            placeholder="아이디 입력"
            value={formData.user_id}
            onChange={handleChange}
            required 
          />
        </div>

        <div style={inputGroupStyle}>
          <label htmlFor="userpw" style={labelStyle}>비밀번호</label>
          <input 
            type="password" 
            id="userpw" 
            name="user_pw" 
            style={inputStyle} 
            placeholder="비밀번호 입력"
            value={formData.user_pw}
            onChange={handleChange}
            required 
          />
        </div>

        <div style={inputGroupStyle}>
          <label htmlFor="username" style={labelStyle}>이름</label>
          <input 
            type="text" 
            id="username" 
            name="user_name" 
            style={inputStyle} 
            placeholder="실명 입력"
            value={formData.user_name}
            onChange={handleChange}
          />
        </div>

        <button type="submit" style={buttonStyle}>가입하기</button>
      </form>
    </div>
  );
}

// --- 디자인 스타일은 주인님 코드를 그대로 유지했어요! ---

const containerStyle: React.CSSProperties = {
  margin: 0,
  backgroundColor: 'hwb(323 55% 2%)',
  height: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  fontFamily: 'sans-serif',
};

const cardStyle: React.CSSProperties = {
  backgroundColor: 'white',
  padding: '40px',
  width: '350px',
  borderRadius: '20px',
  boxShadow: '0 4px 10px hsl(335, 100%, 69%)',
};

const titleStyle: React.CSSProperties = {
  textAlign: 'left',
  color: 'hsl(329, 100%, 50%)',
  marginBottom: '50px',
};

const inputGroupStyle: React.CSSProperties = {
  marginBottom: '20px',
};

const labelStyle: React.CSSProperties = {
  display: 'block',
  marginBottom: '5px',
  fontWeight: 'bold',
  color: 'hsl(329, 100%, 51%)',
};

const inputStyle: React.CSSProperties = {
  width: '100%',
  padding: '10px',
  border: '1px solid hsl(330, 100%, 50%)',
  borderRadius: '5px',
};

const buttonStyle: React.CSSProperties = {
  width: '100%',
  padding: '12px',
  backgroundColor: 'hsl(321, 100%, 76%)',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  fontSize: '16px',
  cursor: 'pointer',
};