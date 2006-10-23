<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="DTD/xhtml1-strict.dtd" indent="yes" omit-xml-declaration="yes"/>
<xsl:template name="formatCost">
	<xsl:param name="cost"/>
	<xsl:variable name="plat" select="floor($cost div 10000000)"/>
	<xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
	<xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
	<xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
	<xsl:if test="$plat &gt; 0"><xsl:copy-of select="$plat"/>p&#160;</xsl:if>
	<xsl:if test="$gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$gold"/>g&#160;</xsl:if>
	<xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$silver"/>s&#160;</xsl:if>
	<xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$copper"/>c</xsl:if>
</xsl:template>

<xsl:template name="lineBreak">
<xsl:text>
</xsl:text>
</xsl:template>

<xsl:template match="/SCTemplate">
<body>
<center><b>Config Report</b></center><br />
<center><b>Stats</b></center><hr />
<table cellspacing="10" cellpadding="0">
<tr><td>Str:</td><td><xsl:value-of select="Strength" /></td>
<td>Int:</td><td><xsl:value-of select="Intelligence"/></td>
<td>Hits:</td><td><xsl:value-of select="Hits" /></td></tr>
<tr><td>Con:</td><td><xsl:value-of select="Constitution" /></td>
<td>Pie:</td><td><xsl:value-of select="Piety" /></td>
<td>Power:</td><td><xsl:value-of select="Power" /></td></tr>
<tr><td>Dex:</td><td><xsl:value-of select="Dexterity" /></td>
<td>Cha:</td><td><xsl:value-of select="Charisma" /></td></tr>
<tr><td>Qui:</td><td><xsl:value-of select="Quickness" /></td>
<td>Emp:</td><td><xsl:value-of select="Empathy" /></td></tr>
</table><br />
<center><b>Resists</b></center><hr />
<table cellspacing="10" cellpadding="0">
<tr><td>Body:</td><td><xsl:value-of select="Body" /></td>
<td>Energy:</td><td><xsl:value-of select="Energy" /></td>
<td>Crush:</td><td><xsl:value-of select="Crush" /></td></tr>
<tr><td>Cold:</td><td><xsl:value-of select="Cold" /></td>
<td>Matter:</td><td><xsl:value-of select="Matter" /></td>
<td>Thrust:</td><td><xsl:value-of select="Thrust" /></td></tr>
<tr><td>Heat:</td><td><xsl:value-of select="Heat" /></td>
<td>Spirit:</td><td><xsl:value-of select="Spirit" /></td>
<td>Slash:</td><td><xsl:value-of select="Slash" /></td></tr>
</table><br />
<!--
<center><b>Skills</b></center><hr />


<skills/><br />
<center><b>Focus</b></center><hr />
<foci/><br />
<center><b>Cap Increases</b></center><hr />
<capbonuses/><br />
<center><b>Other Bonuses</b></center><hr />
<otherbonuses/><br />
-->
<center><b>Piece Listing</b></center><hr />
<xsl:for-each select="SCItem">
	<xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
		<table>
		<tr><td colspan="4"><b><xsl:value-of select="Location" /></b></td></tr>
		<tr><td colspan="4">Name: <xsl:value-of select="Name"/></td></tr>
		<tr><td colspan="4">Level: <xsl:value-of select="Level"/>
		&#160;&#160;&#160;Quality: <xsl:value-of select="ItemQuality"/>
		&#160;&#160;&#160;AF/DPS: <xsl:value-of select="AFDPS"/>
		&#160;&#160;&#160;Bonus: <xsl:value-of select="Bonus"/></td></tr>
		<xsl:if test="ActiveState = 'drop'">
			<tr><td colspan="4">Imbue Points: <xsl:value-of select="format-number(sum(SLOT/Imbue), '##.0')"/>
			of <xsl:value-of select="format-number(ItemImbue, '##.0')"/>
			&#160;&#160;&#160;Quality: <xsl:value-of select="ItemQuality"/>
			&#160;&#160;&#160;Overcharge: <xsl:value-of select="Overcharge"/></td></tr>
		</xsl:if>
		<xsl:for-each select="SLOT">
			<xsl:variable name="slotnum">
				<xsl:value-of select="number(@Number) + 1"/>
			</xsl:variable>
			<xsl:if test="Type != 'Unused'">
				<xsl:choose>
					<xsl:when test="number(@Number) &lt;= 4 and ../ActiveState = 'player'">
						<tr><td>Gem <xsl:copy-of select="$slotnum"/>:&#160;</td>
                                                <td align="right"><xsl:value-of select="Amount"/>&#160;</td>
						<td><xsl:value-of select="Effect"/>&#160;</td>
                                                <td> - <xsl:value-of select="Qua"/> <xsl:value-of select="Name"/></td></tr>
					</xsl:when>
					<xsl:otherwise>
						<tr><td>Effect <xsl:copy-of select="$slotnum"/>:&#160;</td>
						<td align="right"><xsl:value-of select="Amount"/>&#160;</td>
						<td><xsl:value-of select="Effect"/>&#160;</td>
						<td>
						<xsl:if test="../ActiveState = 'player'">
							 - <xsl:value-of select="Name"/>
						</xsl:if>
						</td></tr>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
		</xsl:for-each>
		<tr><td colspan="4">Utility: <xsl:value-of select="Utility"/></td></tr>
		<xsl:if test="ActiveState = 'player'">
			<tr><td colspan="4">Cost: 
				<xsl:call-template name="formatCost">
					<xsl:with-param name="cost" select="Cost"/>
				</xsl:call-template>
			&#160;&#160;&#160;Price: 
				<xsl:call-template name="formatCost">
					<xsl:with-param name="cost" select="Price"/>
				</xsl:call-template>
			</td></tr>
		</xsl:if>
                <tr><td colspan="4">&#160;</td></tr>
                </table>
	</xsl:if>
</xsl:for-each>
</body>
</xsl:template>
</xsl:stylesheet>
