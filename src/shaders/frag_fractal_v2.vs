#version 330 core

in vec2 uv;
uniform float iTime;
uniform vec2 iResolution;
uniform vec2 iMouse;
out vec4 frag_color;


vec3 palette(float t, vec3 a, vec3 b, vec3 c, vec3 d)
{
    return a + b*cos(6.28318*(c*t+d));
}

void main()
{	
    vec2 UV = (uv-0.5)*2;
    vec3 finalColor = vec3(0.0);

    float d = length(UV);
    vec3 op = vec3( d-iTime, UV/d );

	frag_color = vec4(op , 1.0);
}